"""
Constants for the control logic of the computer with a flags register. Each control logic signal is controlled by a
single bit of the output of a lookup table. The order, from most to lease significant output bit is below. The ordering
is based on the physical
layout of the system:

  - HLT (Halt)
  - ADR (Address Register)
  - RMI (RAM In)
  - RMO (RAM Out)
  - FLG (Flags Register In)
  - IRO (Instruction Register Out)
  - IRI (Instruction Register In)
  - SGN (Signed Integer)
  - ORI (Output Register In)
  - SUB (Subtraction)
  - ALU (ALU Out)
  - BRO (B Register Out)
  - BRI (B Register In)
  - ARO (A Register Out)
  - ARI (A Register In)
  - PCO (Program Counter Out)
  - PCI (Program Counter In)
  - PCE (Program Counter Enable)


To create a microcode, constants can be bitwise ORed together. For example, the two microcodes for a 'fetch' would be:

             PCO | ADR             Program Counter Out -> Address Register
             RMO | IRI | PCE       RAM Out -> Instruction Register In + Program Counter Enable


Note: The order of the operands does not matter, however, a pattern of FROM -> TO is followed, where possible.

Underscore are included in the constants below for visual clarity
"""
HLT = 0b10_00000000_00000000
ADR = 0b01_00000000_00000000
RMI = 0b00_10000000_00000000
RMO = 0b00_01000000_00000000
FLG = 0b00_00100000_00000000
IRO = 0b00_00010000_00000000
IRI = 0b00_00001000_00000000
ORI = 0b00_00000100_00000000
SGN = 0b00_00000010_00000000
SUB = 0b00_00000001_00000000
ALU = 0b00_00000000_10000000
BRO = 0b00_00000000_01000000
BRI = 0b00_00000000_00100000
ARO = 0b00_00000000_00010000
ARI = 0b00_00000000_00001000
PCO = 0b00_00000000_00000100
PCE = 0b00_00000000_00000010
PCI = 0b00_00000000_00000001

"""
Jump command binary patterns/indices in instruction list
"""
JMPA = 0b1001
JMPZ = 0b1010
JMPS = 0b1011
JMPC = 0b1100

"""
Mirocodes for the 16 possible instructions. Each microcode could be up to 4 instructions long. 
"""
INSTRUCTIONS = [
  [PCO|ADR,   RMO|IRI|PCE, 0,               0           ],  # 0b0000 --- 0x0 --- NOOP --- No Operation
  [PCO|ADR,   RMO|IRI|PCE, IRO|ADR,         RMO|ARI     ],  # 0b0001 --- 0x1 --- LDAR --- Load A From RAM
  [PCO|ADR,   RMO|IRI|PCE, IRO|ARI,         0           ],  # 0b0010 --- 0x2 --- LDAD --- Load A Direct
  [PCO|ADR,   RMO|IRI|PCE, IRO|ADR,         RMO|BRI     ],  # 0b0011 --- 0x3 --- LDBR --- Load B From RAM
  [PCO|ADR,   RMO|IRI|PCE, IRO|BRI,         0           ],  # 0b0100 --- 0x4 --- LDBD --- Load B Direct
  [PCO|ADR,   RMO|IRI|PCE, IRO|ADR,         ARO|RMI     ],  # 0b0101 --- 0x5 --- SAVA --- Save A to RAM
  [PCO|ADR,   RMO|IRI|PCE, IRO|ADR,         BRO|RMI     ],  # 0b0110 --- 0x6 --- SAVB --- Save B to RAM
  [PCO|ADR,   RMO|IRI|PCE, ALU|ARI|FLG,     0           ],  # 0b0111 --- 0x7 --- ADAB --- Add B to A
  [PCO|ADR,   RMO|IRI|PCE, ALU|SUB|ARI|FLG, 0           ],  # 0b1000 --- 0x8 --- SUAB --- Subtract B from A
  [PCO|ADR,   RMO|IRI|PCE, IRO|PCI,         0           ],  # 0b1001 --- 0x9 --- JMPA --- Jump Always
  [PCO|ADR,   RMO|IRI|PCE, 0,               0           ],  # 0b1010 --- 0xA --- JMPZ --- Jump Zero
  [PCO|ADR,   RMO|IRI|PCE, 0,               0           ],  # 0b1011 --- 0xB --- JMPS --- Jump Significant/sign
  [PCO|ADR,   RMO|IRI|PCE, 0,               0           ],  # 0b1100 --- 0xC --- JMPC --- Jump Carry
  [PCO|ADR,   RMO|IRI|PCE, IRO|ADR,         RMO|ORI     ],  # 0b1101 --- 0xD --- OUTU --- Output Unsigned Integer
  [PCO|ADR,   RMO|IRI|PCE, IRO|ADR,         RMO|ORI|SGN ],  # 0b1110 --- 0xE --- OUTS --- Output Signed Integer
  [PCO|ADR,   RMO|IRI|PCE, HLT,             0           ],  # 0b1111 --- 0xF --- HALT --- Halt
]

"""
Write the microcode patterns for each instructions to a hex file. 

Each row/individual microcode is accessed by some pattern inputted into the lookup table. The first 3 bits correspond to 
the flags status, the 4 middle bits of the input pattern correspond to the specific instruction, and the last 2 bits 
corresponds to an individual microcode for the corresponding instruction.

  FLAGS | INSTRCT | MICROCODE
  0 0 0 | 0 0 0 0 | 0 0 
  
Each group of 16 instructions are stacked for the 8 possible status flag states. 
  0 0 0 --- No flags
  0 0 1 --- Zero flag set
  0 1 0 --- Significant/sign flag set
  0 1 1 --- Significant/sign and zero flags set 
  1 0 0 --- Carry flag set
  1 0 1 --- Carry and zero flags set
  1 0 1 --- Carry and significant/sign flags set
  1 1 1 --- Carry, significant/sign, and zero flags set
 
The special jump condition instructions are modified to act as a jump for their respective status flag groupings. This 
way, if a status flag is set and being input into the control logic look up table, it will act as a jump. Otherwise, it
acts as a NOOP. For example, consider the JMPZ instruction:

  X X 0 | 1 0 1 0 | X X --- If the zero status flag is not set, do not jump/do NOOP
  X X 1 | 1 0 1 0 | X X --- If the zero status flag is set, jump to specified address
   
"""
with open("control_logic_with_flag_patterns_for_look_up_table.hex", "w") as hex_file:
  hex_file.write("v2.0 raw\n")
  for flags_state in range(8):
    for i, instruction in enumerate(INSTRUCTIONS):
      if (i == JMPZ and flags_state & 0b001 != 0 or
              i == JMPS and flags_state & 0b010 != 0 or
              i == JMPC and flags_state & 0b100 != 0):
        # If special jump instruction and the flag is set, do jump instruction microcodes
        hex_file.writelines(f"{hex(microcode_pattern)}\n" for microcode_pattern in INSTRUCTIONS[JMPA])
      else:
        hex_file.writelines(f"{hex(microcode_pattern)}\n" for microcode_pattern in instruction)
