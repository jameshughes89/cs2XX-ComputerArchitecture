"""
Constants for the 7-segment display. The display is laid out as follows:

              a
              -
            f|g|b
              - 
            e| |c
              - .
              d h

Labelling is clockwise, starting at twelve o'clock, with the centre being the last value. 
There is a decimal point, but that is not be used here. Based on the physical layout of the 
output module as designed in DIGITAL, the bitstring ordering is hgfedcba. The most significant 
bit is always 0 since the decimal is not used. 
"""

ZERO      = 0b00111111  # 0x3F
ONE       = 0b00000110  # 0x06
TWO       = 0b01011011  # 0x5B
THREE     = 0b01001111  # 0x4F
FOUR      = 0b01100110  # 0x66
FIVE      = 0b01101101  # 0x6D
SIX       = 0b01111101  # 0x7D
SEVEN     = 0b00000111  # 0x07
EIGHT     = 0b01111111  # 0x7F
NINE      = 0b01101111  # 0x6F
NEGATIVE  = 0b01000000  # 0x80
DIGITS = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]
