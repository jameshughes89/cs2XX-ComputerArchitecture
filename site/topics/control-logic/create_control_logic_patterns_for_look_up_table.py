"""
Constants for the control logic of the computer. Each control logic signal is controlled by a single bit of the output
of a lookup table. The order, from most to lease significant output bit is below. The orderins is based on the pysical
layout of the system:

  - IRO (Instruction Register Out)
  - IRI (Instruction Register In)
  - RMO (RAM Out)
  - RMI (RAM In)
  - ADR (Address Register)
  - HLT (Halt)
  - PCE (Program Counter Enable)
  - PCI (Program Counter In)
  - PCO (Program Counter Out)
  - ARI (A Register In)
  - ARO (A Register Out)
  - BRI (B Register In)
  - BRO (B Register Out)
  - ALU (ALU Out)
  - SUB (Subtraction)
  - ORI (Output Register In)
  - SGN (Signed Integer)


To create a microcode, constants can be bitwise ORed together. For example, the two microcodes for a 'fetch' would be:

             PCO | ADR             Program Counter Out -> Address Register
             RMO | IRI | PCE       RAM Out -> Instruction Register In + Program Counter Enable


Note: The order of the operands does not matter, however, a pattern of FROM -> TO is followed, where possible.

Underscore are included in the constants below for visual clarity
"""
IRO = 0b1_00000000_00000000
IRI = 0b0_10000000_00000000
RMO = 0b0_01000000_00000000
RMI = 0b0_00100000_00000000
ADR = 0b0_00010000_00000000
HLT = 0b0_00001000_00000000
PCE = 0b0_00000100_00000000
PCI = 0b0_00000010_00000000
PCO = 0b0_00000001_00000000
ARI = 0b0_00000000_10000000
ARO = 0b0_00000000_01000000
BRI = 0b0_00000000_00100000
BRO = 0b0_00000000_00010000
ALU = 0b0_00000000_00001000
SUB = 0b0_00000000_00000100
ORI = 0b0_00000000_00000010
SGN = 0b0_00000000_00000001


"""
Mirocodes for the 16 possible instructions. Each microcode could be up to 8 instructions long, but currently the max is 
5, thus, there is some "wasted" space in the lookup table. Not all 16 operations are implemented here. 
"""
INSTRUCTIONS = [
  [PCO|RMI,   RMO|IRI|PCE, 0,       0,        0,            0, 0, 0],    # 0000 --- NOOP --- No Operation
  [PCO|RMI,   RMO|IRI|PCE, IRO|ADR, RMO|ARI,  0,            0, 0, 0],    # 0001 --- LDAR --- Load A From RAM
  [PCO|RMI,   RMO|IRI|PCE, IRO|ARI, 0,        0,            0, 0, 0],    # 0010 --- LDAD --- Load A Direct
  [PCO|RMI,   RMO|IRI|PCE, IRO|ADR, RMO|BRI,  0,            0, 0, 0],    # 0011 --- LDBR --- Load B From RAM
  [PCO|RMI,   RMO|IRI|PCE, IRO|BRI, 0,        0,            0, 0, 0],    # 0100 --- LDBD --- Load B Direct
  [PCO|RMI,   RMO|IRI|PCE, IRO|ADR, ARO|RMI,  0,            0, 0, 0],    # 0101 --- SAVA --- Save A to RAM
  [PCO|RMI,   RMO|IRI|PCE, IRO|ADR, BRO|RMI,  0,            0, 0, 0],    # 0110 --- SAVB --- Save B to RAM
  [PCO|RMI,   RMO|IRI|PCE, IRO|ADR, RMO|BRI,  ALU|ARI,      0, 0, 0],    # 0111 --- ADDB --- Add to A
  [PCO|RMI,   RMO|IRI|PCE, IRO|ADR, RMO|BRI,  ALU|SUB|ARI,  0, 0, 0],    # 1000 --- SUBB --- Subtract from A
  [PCO|RMI,   RMO|IRI|PCE, 0,       0,        0,            0, 0, 0],    # 1001 --- JUMP --- Jump
  [PCO|RMI,   RMO|IRI|PCE, 0,       0,        0,            0, 0, 0],    # 1010 --- NOOP --- No Operation
  [PCO|RMI,   RMO|IRI|PCE, 0,       0,        0,            0, 0, 0],    # 1011 --- NOOP --- No Operation
  [PCO|RMI,   RMO|IRI|PCE, 0,       0,        0,            0, 0, 0],    # 1100 --- NOOP --- No Operation
  [PCO|RMI,   RMO|IRI|PCE, 0,       0,        0,            0, 0, 0],    # 1101 --- OUTU --- Output Unsigned Integer
  [PCO|RMI,   RMO|IRI|PCE, 0,       0,        0,            0, 0, 0],    # 1110 --- OUTS --- Output Signed Integer
  [PCO|RMI,   RMO|IRI|PCE, HLT,     0,        0,            0, 0, 0],    # 1111 --- HALT --- Halt
]

