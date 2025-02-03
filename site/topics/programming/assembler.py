import sys

OPERATORS = {
    "NOOP": 0b0000,
    "LDAR": 0b0001,
    "LDAD": 0b0010,
    "LDBR": 0b0011,
    "LDBD": 0b0100,
    "SAVA": 0b0101,
    "SAVB": 0b0110,
    "ADDB": 0b0111,
    "SUBB": 0b1000,
    "JMPA": 0b1001,
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
    "OUTU",
    "OUTS",
}

def parse_number(number_string:str) -> int:
    try:
        if number_string[:2] == "0b":
            number = int(number_string, 2)
        elif number_string[:2] == "0x":
            number = int(number_string, 16)
        else:
            number = int(number_string)
    except ValueError:
        raise ValueError(f"Cannot parse operand {number_string}")
    return number


file_to_assemble = sys.argv[1]
with open(file_to_assemble) as file:
    program_list = file.read().strip().split("\n")

if len(program_list) > 16:
    raise ValueError(f"Program length of {len(program_list)} exceeds maximum size of 16 bytes")

machine_code = [0x00] * 16
for i, raw_program_line in enumerate(program_list):
    line = raw_program_line.split()
    if line[0].isalpha():
        try:
            operator = OPERATORS[line[0]]
        except KeyError:
            raise ValueError(f"Unknown operator {line[0]}")
        if line[0] not in HAS_OPERAND:
            if len(line) > 1:
                raise ValueError(f"Operator {line[0]} requires no operand")
            operand = 0
        else:
            if len(line) != 2:
                raise ValueError(f"Operator {line[0]} requires one operand")
            operand = parse_number(line[1])
            if operand >= 16:
                raise ValueError(f"Operand value {line[1]} too large")

        machine_code_line = (operator << 4) | operand
    else:
        number = parse_number(line[0])
        if number >= 256:
            raise ValueError(f"Data value {line[0]} too large")
        machine_code_line = number
    machine_code[i] = machine_code[i] | machine_code_line

with open("a.hex", "w") as hex_file:
    hex_file.write("v2.0 raw\n")
    hex_file.writelines([f"0x{code:02x}\n" for code in machine_code])