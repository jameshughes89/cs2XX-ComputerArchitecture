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


def program_string_to_list_of_instructions(program:str) -> list[str]:
    program_list = program.strip().split("\n")
    if len(program_list) > 16:
        raise ValueError(f"Program length of {len(program_list)} exceeds maximum size of 16 bytes")
    return program_list


def parse_instruction_operator(instruction:list[str]) -> int:
    try:
        operator = OPERATORS[instruction[0]]
    except KeyError:
        raise ValueError(f"Unknown operator {instruction[0]}")
    return operator


def parse_instruction_operand(instruction:list[str]) -> int:
    if instruction[0] not in HAS_OPERAND:
        if len(instruction) > 1:
            raise ValueError(f"Operator {instruction[0]} requires no operand")
        operand = 0
    else:
        if len(instruction) != 2:
            raise ValueError(f"Operator {instruction[0]} requires one operand")
        operand_string = instruction[1]
        try:
            if operand_string[:2] == "0b":
                operand = int(operand_string, 2)
            elif operand_string[:2] == "0x":
                operand = int(operand_string, 16)
            else:
                operand = int(operand_string)
        except ValueError:
            raise ValueError(f"Cannot parse operand {operand_string}")
        if operand >= 16:
            raise ValueError(f"Operand value {operand_string} too large")
    return operand


def create_assembled_string(machine_codes: list[int]) -> str:
    raw_line = "v2.0 raw\n"
    assembled_program = "".join([f"0x{code:02x}\n" for code in machine_codes])
    return raw_line + assembled_program


if __name__ == "__main__":
    file_to_assemble = sys.argv[1]

    with open(file_to_assemble) as file:
        program_string = file.read()

    instruction_list = program_string_to_list_of_instructions(program_string)
    # PARSE A NUMBER!

    machine_code = [0x00] * 16
    for i, line in enumerate(instruction_list):
        instruction = line.split()
        operator = parse_instruction_operator(instruction)
        operand = parse_instruction_operand(instruction)
        machine_code[i] = machine_code[i] | (operator << 4 | operand)


    assembled_string = create_assembled_string(machine_code)
    with open("a.hex", "w") as hex_file:
        hex_file.write(assembled_string)