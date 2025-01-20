"""
Constants for the control logic of the computer. Each control logic signal is controlled by a single bit of the output
of a lookup table. The order, from most to lease significant output bit is below. The ordering is based on the physical
layout of the system:

  - HLT (Halt)
  - ADR (Address Register)
  - RMI (RAM In)
  - RMO (RAM Out)
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
HLT = 0b1_00000000_00000000
ADR = 0b0_10000000_00000000
RMI = 0b0_01000000_00000000
RMO = 0b0_00100000_00000000
IRO = 0b0_00010000_00000000
IRI = 0b0_00001000_00000000
SGN = 0b0_00000100_00000000
ORI = 0b0_00000010_00000000
SUB = 0b0_00000001_00000000
ALU = 0b0_00000000_10000000
BRO = 0b0_00000000_01000000
BRI = 0b0_00000000_00100000
ARO = 0b0_00000000_00010000
ARI = 0b0_00000000_00001000
PCO = 0b0_00000000_00000100
PCE = 0b0_00000000_00000010
PCI = 0b0_00000000_00000001

"""
Mirocodes for the 16 possible instructions. Each microcode could be up to 8 instructions long, but currently the max is 
5, thus, there is some "wasted" space in the lookup table. Not all 16 operations are implemented here. 
"""
INSTRUCTIONS = [
  [PCO|ADR,   RMO|IRI|PCE, 0,           0           ],  # 0b0000 --- 0x0 --- NOOP --- No Operation
  [PCO|ADR,   RMO|IRI|PCE, IRO|ADR,     RMO|ARI     ],  # 0b0001 --- 0x1 --- LDAR --- Load A From RAM
  [PCO|ADR,   RMO|IRI|PCE, IRO|ARI,     0           ],  # 0b0010 --- 0x2 --- LDAD --- Load A Direct
  [PCO|ADR,   RMO|IRI|PCE, IRO|ADR,     RMO|BRI     ],  # 0b0011 --- 0x3 --- LDBR --- Load B From RAM
  [PCO|ADR,   RMO|IRI|PCE, IRO|BRI,     0           ],  # 0b0100 --- 0x4 --- LDBD --- Load B Direct
  [PCO|ADR,   RMO|IRI|PCE, IRO|ADR,     ARO|RMI     ],  # 0b0101 --- 0x5 --- SAVA --- Save A to RAM
  [PCO|ADR,   RMO|IRI|PCE, IRO|ADR,     BRO|RMI     ],  # 0b0110 --- 0x6 --- SAVB --- Save B to RAM
  [PCO|ADR,   RMO|IRI|PCE, ALU|ARI,     0           ],  # 0b0111 --- 0x7 --- ADDB --- Add B to A
  [PCO|ADR,   RMO|IRI|PCE, ALU|SUB|ARI, 0           ],  # 0b1000 --- 0x8 --- SUBB --- Subtract B from A
  [PCO|ADR,   RMO|IRI|PCE, IRO|PCI,     0           ],  # 0b1001 --- 0x9 --- JMPA --- Jump Always
  [PCO|ADR,   RMO|IRI|PCE, 0,           0           ],  # 0b1010 --- 0xA --- NOOP --- No Operation
  [PCO|ADR,   RMO|IRI|PCE, 0,           0           ],  # 0b1011 --- 0xB --- NOOP --- No Operation
  [PCO|ADR,   RMO|IRI|PCE, 0,           0           ],  # 0b1100 --- 0xC --- NOOP --- No Operation
  [PCO|ADR,   RMO|IRI|PCE, IRO|ADR,     RMO|ORI     ],  # 0b1101 --- 0xD --- OUTU --- Output Unsigned Integer
  [PCO|ADR,   RMO|IRI|PCE, IRO|ADR,     RMO|ORI|SGN ],  # 0b1110 --- 0xE --- OUTS --- Output Signed Integer
  [PCO|ADR,   RMO|IRI|PCE, HLT,         0           ],  # 0b1111 --- 0xF --- HALT --- Halt
]

"""
Write the microcode patterns for each instructions to a hex file. 

Each row/individual microcode is accessed by some pattern inputted into the lookup table. The 4 most significant bits of
the input pattern correspond to the specific instruction, and the last two bits corresponds to an individual microcode 
for the corresponding instruction.

  INSTRUCTION | MICROCODE
      0 0 0 0 | 0 0 
  
For example, consider LDAR (Load A from RAM)

      0 0 0 1 | 0 0 --- Program Counter Out + Address Register In 
      0 0 0 1 | 0 1 --- RAM Out + Instruction Register In + Program Counter Enable
      0 0 0 1 | 1 0 --- Instruction Register Out +  Address Register In 
      0 0 0 1 | 1 1 --- RAM Out + A Register In 
  
"""
with open("control_logic_patterns_for_look_up_table.hex", "w") as hex_file:
  hex_file.write("v2.0 raw\n")
  for instruction in INSTRUCTIONS:
    hex_file.writelines(f"{hex(microcode_pattern)}\n" for microcode_pattern in instruction)