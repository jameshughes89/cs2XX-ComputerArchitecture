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

file_to_assemble = sys.argv[1]
with open(file_to_assemble) as file:
    program = file.read().split("\n")

if len(program) > 16:
    raise RuntimeError(f"Program length of {len(program)} exceeds maximum size of 16 bytes")


machine_code = [0x00] * 16
for i, line in enumerate(program):
    instruction = line.split()
    try:
        operator = OPERATORS[instruction[0]]
    except KeyError:
        raise RuntimeError(f"Unknown operator {instruction[0]}")
    if instruction[0] not in HAS_OPERAND:
        if len(instruction) > 1:
            raise RuntimeError(f"Operator {instruction[0]} requires no operand")
        operand = 0
    else:
        if len(instruction) != 2:
            raise RuntimeError(f"Operator {instruction[0]} requires one operand")
        operand_string = instruction[1]

        try:
            if operand_string[:2] == "0b":
                operand = int(operand_string, 2)
            elif operand_string[:2] == "0x":
                operand = int(operand_string, 16)
            else:
                operand = int(operand_string)
        except ValueError:
            raise RuntimeError(f"Cannot parse operand {operand_string}")

    machine_code[i] = machine_code[i] | (operator << 4 | operand)

with open("a.hex", "w") as hex_file:
    hex_file.write("v2.0 raw\n")
    hex_file.writelines([f"{hex(code):04}\n" for code in machine_code])