"""
Constants for the control logic of the CPU/computer. The values each constant has is dependent
on the physical configuration of the CPU/computer. In other words, different physical
configurations of the CPU/computer would require a change to the constant values. The current
configuration is arbitrary. There are a total of 16 modules (for lack of a better term) on the
CPU/computer, but each EEPROM only has 8 data lines. The solution to this problem is to simply 
use two EEPROMS --- one for the first 8, the other for the other 8. Each constant will be 
represented as a 16 bit integer and, depending on which EEPROM is being programed, some 8 bit
shifts may be required.

The configuration of the EEPROMs and the individual modules they correspond to are as follows:

           HLT MRI RMI RMO IRO IRI ARI ARO    AUO SUB BRI ORI PCE PCO JMP XXX             
            F   E   D   C   B   A   9   8      7   6   5   4   3   2   1   0

To use these constants for writing a single microcode, simply OR (|) the corresponding constants 
together. For example, the two microcodes for a 'fetch' would be:

             PCO | MRI             Program Counter Out -> Memory Register IN
             RMO | IRI | PCE       RAM Out -> Instruction Register In + Program Counter Enable

Note: The order of the constants is simply because I like the OUT before the IN, like FROM -> TO,
but this is entirely arbitrary.                           
"""

HLT = 0b1000000000000000  # Halt
MRI = 0b0100000000000000  # Memory Address Register In
RMI = 0b0010000000000000  # RAM In
RMO = 0b0001000000000000  # RAM Out
IRI = 0b0000100000000000  # Instruction Register In
IRO = 0b0000010000000000  # Instruction Register OUT
ARI = 0b0000001000000000  # 'A' Register In
ARO = 0b0000000100000000  # 'A' Register Out

AUO = 0b0000000010000000  # ALU Out
SUB = 0b0000000001000000  # Subtraction
BRI = 0b0000000000100000  # 'B' Register In
ORI = 0b0000000000010000  # Output Register In
PCE = 0b0000000000001000  # Program Counter Enable
PCO = 0b0000000000000100  # Program Counter Out
JMP = 0b0000000000000010  # Jump
XXX = 0b0000000000000001  # Some jump register, I can't rememeber right now; I'll find out later \shrug

"""
Mirocodes for the 16 instructions. Each microcode could be up to 8 instructions long, but currently 
the max is 5, thus, there is some "wasted" RAM (though, this only uses 128 Bytes on each of the two 
EEPROMs that both have 2048 Bytes).
"""
INSTRUCTIONS = [
  [PCO|MRI,   RMO|IRI|PCE, 0,       0,        0,        0, 0, 0],    # 0000 --- NOP --- No Operation
  [PCO|MRI,   RMO|IRI|PCE, IRO|MRI, RMO|ARI,  0,        0, 0, 0],    # 0001 --- LDA --- Load A Register
  [PCO|MRI,   RMO|IRI|PCE, IRO|MRI, RMO|BRI,  AUO|ARI,  0, 0, 0],    # 0010 --- ADD --- Add
  [PCO|MRI,   RMO|IRI|PCE, 0,       0,        0,        0, 0, 0],    # 0011 --- NOP --- No Operation
  [PCO|MRI,   RMO|IRI|PCE, 0,       0,        0,        0, 0, 0],    # 0100 --- NOP --- No Operation
  [PCO|MRI,   RMO|IRI|PCE, 0,       0,        0,        0, 0, 0],    # 0101 --- NOP --- No Operation
  [PCO|MRI,   RMO|IRI|PCE, 0,       0,        0,        0, 0, 0],    # 0110 --- NOP --- No Operation
  [PCO|MRI,   RMO|IRI|PCE, 0,       0,        0,        0, 0, 0],    # 0111 --- NOP --- No Operation
  [PCO|MRI,   RMO|IRI|PCE, 0,       0,        0,        0, 0, 0],    # 1000 --- NOP --- No Operation
  [PCO|MRI,   RMO|IRI|PCE, 0,       0,        0,        0, 0, 0],    # 1001 --- NOP --- No Operation
  [PCO|MRI,   RMO|IRI|PCE, 0,       0,        0,        0, 0, 0],    # 1010 --- NOP --- No Operation
  [PCO|MRI,   RMO|IRI|PCE, 0,       0,        0,        0, 0, 0],    # 1011 --- NOP --- No Operation
  [PCO|MRI,   RMO|IRI|PCE, 0,       0,        0,        0, 0, 0],    # 1100 --- NOP --- No Operation
  [PCO|MRI,   RMO|IRI|PCE, 0,       0,        0,        0, 0, 0],    # 1101 --- NOP --- No Operation
  [PCO|MRI,   RMO|IRI|PCE, ARO|ORI, 0,        0,        0, 0, 0],    # 1110 --- OTA --- Output A Register
  [PCO|MRI,   RMO|IRI|PCE, HLT,     0,        0,        0, 0, 0],    # 1111 --- HLT --- Halt
]
