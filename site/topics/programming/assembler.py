import re
import sys

OPERATORS = {
    "NOOP": 0b0000,
    "LDAR": 0b0001,
    "LDAD": 0b0010,
    "LDBR": 0b0011,
    "LDBD": 0b0100,
    "SAVA": 0b0101,
    "SAVB": 0b0110,
    "ADAB": 0b0111,
    "SUAB": 0b1000,
    "JMPA": 0b1001,
    "JMPZ": 0b1010,
    "JMPS": 0b1011,
    "JMPC": 0b1100,
    "OUTU": 0b1101,
    "OUTS": 0b1110,
    "HALT": 0b1111,
}
HAS_OPERAND = {
    "LDAR",
    "LDAD",
    "LDBR",
    "LDBD",
    "SAVA",
    "SAVB",
    "JMPA",
    "JMPZ",
    "JMPS",
    "JMPC",
    "OUTU",
    "OUTS",
}
VALID_SYNTAX = {
    r"NOOP",
    r"LDAR\s+\b(0x[0-9a-fA-F]+|0b[0-1]+|[0-9]+)\b",
    r"LDAD\s+-?\b(0x[0-9a-fA-F]+|0b[0-1]+|[0-9]+)\b",
    r"LDBR\s+\b(0x[0-9a-fA-F]+|0b[0-1]+|[0-9]+)\b",
    r"LDBD\s+-?\b(0x[0-9a-fA-F]+|0b[0-1]+|[0-9]+)\b",
    r"SAVA\s+\b(0x[0-9a-fA-F]+|0b[0-1]+|[0-9]+)\b",
    r"SAVB\s+\b(0x[0-9a-fA-F]+|0b[0-1]+|[0-9]+)\b",
    r"ADAB",
    r"SUAB",
    r"JMPA\s+\b(0x[0-9a-fA-F]+|0b[0-1]+|[0-9]+)\b",
    r"JMPZ\s+\b(0x[0-9a-fA-F]+|0b[0-1]+|[0-9]+)\b",
    r"JMPS\s+\b(0x[0-9a-fA-F]+|0b[0-1]+|[0-9]+)\b",
    r"JMPC\s+\b(0x[0-9a-fA-F]+|0b[0-1]+|[0-9]+)\b",
    r"OUTU\s+\b(0x[0-9a-fA-F]+|0b[0-1]+|[0-9]+)\b",
    r"OUTS\s+\b(0x[0-9a-fA-F]+|0b[0-1]+|[0-9]+)\b",
    r"HALT",
    r"^-?\b(0x[0-9a-fA-F]+|0b[0-1]+|[0-9]+)\b",
}

def parse_number(number_string:str) -> int:
    """
    Convert a string of a number to a decimal integer representable with the specified number of bits. This function
    will work with binary (0bXXXX), hex (0xXX), decimal, etc.

    :param number_string: String of a number to be converted.
    :return: Value of the string as a decimal integer.
    """
    try:
        number = int(eval(number_string))
    except (ValueError, SyntaxError):
        raise ValueError(f"Cannot parse operand {number_string}")
    return number


def verify_number_and_fix_negative(number:int, max_bits:int) -> int:
    """
    Verify that the number fits in the specified number of bits and convert to a signed, 2s compliment binary pattern
    where necessary.

    If the number is negative, this function applies the 2s compliment conversion since Python does not store negative
    integers in a 2s compliment format. For example, the number -10 should be converted to the 2s compliment binary
    pattern 0b0110. Since Python treats all binary patterns are unsigned ints, this would mean this function returns the
    integer 6 in this case.

    :param number: Number to be verified and converted
    :param max_bits: Maximum number of bits the number can be stored in.
    :return: Decimal version of the number (may be signed int binary pattern's decimal value).
    """
    # max_bits + 2 to account for the 0b in the string
    # negative numbers are representable in max_bits - 1, but require +1 for the negative sign
    # len(bin(number + 1)) when negative to account for edge case of the min negative number needing 1 more bit 
    if (number < 0 and len(bin(number + 1)) > max_bits + 2 or
            number >= 0 and len(bin(number)) > max_bits + 2):
        raise ValueError(f"Data value {number} cannot be represented with {max_bits} bits.")
    if number < 0:
        number = ((2**max_bits - 1 ) ^ number * -1) + 1
    return number


def verify_syntax_return_string(program_line):
    """
    Verifies that a given program line is valid syntax for the assembler. If valid, this function returns the string,
    otherwise the function raises a ValueError.

    :param program_line:
    :raise ValueError: If the program line does not match a valid syntax pattern.
    :return: Returns a valid program line
    """
    for syntax in VALID_SYNTAX:
        syntax_match = re.match(syntax, program_line)
        if syntax_match:
            return syntax_match[0]
    raise ValueError(f"Invalid operator and/or operand {program_line}")


if len(sys.argv) != 2:
    raise ValueError(f"Assembler requires exactly one argument specifying a file name, {len(sys.argv) - 1} given")

file_to_assemble = sys.argv[1]
with open(file_to_assemble) as file:
    program_list = [line.strip() for line in file.readlines() if line.strip()]

if len(program_list) > 16:
    raise ValueError(f"Program length of {len(program_list)} exceeds maximum size of 16 bytes")

machine_code = []
for i, raw_program_line in enumerate(program_list):
    verified_program_line = verify_syntax_return_string(raw_program_line)
    line = verified_program_line.split()
    if line[0].isalpha():
        operator = OPERATORS[line[0]]
        if line[0] not in HAS_OPERAND:
            operand = 0
        else:
            operand = parse_number(line[1])
            operand = verify_number_and_fix_negative(operand, 4)
        machine_code_line = (operator << 4) | operand
    else:
        machine_code_line = parse_number(line[0])
        machine_code_line = verify_number_and_fix_negative(machine_code_line, 8)
    machine_code.append(machine_code_line)

with open("a.hex", "w") as hex_file:
    hex_file.write("v2.0 raw\n")
    hex_file.writelines([f"0x{code:02x}\n" for code in machine_code])