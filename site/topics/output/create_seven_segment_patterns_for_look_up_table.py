"""
Constants for the 7-segment display. The display is laid out as follows:

              a
              -
            f|g|b
              - 
            e| |c
              - .
              d h

Labelling is clockwise, starting at twelve o'clock, with the centre being the last value. There is a decimal point, but
that is not be used here. Based on the physical layout of the output module as designed in DIGITAL, the bitstring
ordering is hgfedcba. The most significant bit is always 0 since the decimal is not used.
"""
# [begin-seven_segment_digit_pattern_constants]
ZERO        = 0b00111111  # 0x3F
ONE         = 0b00000110  # 0x06
TWO         = 0b01011011  # 0x5B
THREE       = 0b01001111  # 0x4F
FOUR        = 0b01100110  # 0x66
FIVE        = 0b01101101  # 0x6D
SIX         = 0b01111101  # 0x7D
SEVEN       = 0b00000111  # 0x07
EIGHT       = 0b01111111  # 0x7F
NINE        = 0b01101111  # 0x6F
DIGITS = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]
# [end-seven_segment_digit_pattern_constants]

"""
Create the three digit patterns for the numbers 0 -- 255. Since each digit is an 8 bit pattern for the seven segment 
display, a total of 24 bits is required to encode the pattern for a three digit number. This is achieved by getting the 
seven segment binary pattern for each digit (hundreds, tens, ones) of the number, bit shifting them to the left 16, 8, 
or 0 bits (depending on which digit they are), and bitwise ORing them together to form the final 24 bit pattern for the 
three digit seven segment display.

For example, consider the number 123, each digit's pattern is as follows
    1   00000110
    2   01011011
    3   01001111

Bit shift the hundreds to the left 16 bits, tens to the left 8 bits, and shift the ones 0 (do nothing). Spaces between
groupings of 8 are included below for visual clarity, but each row is to be considered a single number
    1   00000110 00000000 00000000
    2   00000000 01011011 00000000
    3   00000000 00000000 01001111
    
Finally, bitwise ORing them together effectively puts each digit's part together in a single number
    123 00000110 01011011 01001111
"""
# [begin-unsigned_patterns]
unsigned_three_digit_patterns = []
for i in range(0, 256):
    hundreds_pattern = DIGITS[(i//100) % 10] << 16
    tens_pattern = DIGITS[(i//10) % 10] << 8
    ones_pattern = DIGITS[(i//1) % 10] << 0
    three_digit_pattern = hundreds_pattern | tens_pattern | ones_pattern
    unsigned_three_digit_patterns.append(three_digit_pattern)
# [end-unsigned_patterns]

"""
Create the signed three digit patterns for the numbers -128 -- 127. Following the pattern of 2s complement, the numbers
will be ordered 0 -- 127, then -128 -- -1. Based on the configuration of the output module in DIGITAL, the left most
seven segment display will show a negative when the most significant bit of a 25 bit pattern is high (three groups of 8 
bits plus the bit for the negative sign).  
"""
# [begin-signed_patterns]
signed_three_digit_patterns = []
for i in range(0, 128):
    hundreds_pattern = DIGITS[(i//100) % 10] << 16
    tens_pattern = DIGITS[(i//10) % 10] << 8
    ones_pattern = DIGITS[(i//1) % 10] << 0
    three_digit_pattern = hundreds_pattern | tens_pattern | ones_pattern
    signed_three_digit_patterns.append(three_digit_pattern)

for i in range(-128, 0):
    negation_pattern = 0b1 << 24
    hundreds_pattern = DIGITS[(abs(i)//100) % 10] << 16
    tens_pattern = DIGITS[(abs(i)//10) % 10] << 8
    ones_pattern = DIGITS[(abs(i)//1) % 10] << 0
    three_digit_pattern = negation_pattern | hundreds_pattern | tens_pattern | ones_pattern
    signed_three_digit_patterns.append(three_digit_pattern)
# [end-signed_patterns]

"""
Write the lists to a hex file such that each row corresponds to a bit pattern, starting at 0, and the hex value in that
row corresponds to the seven segment display pattern for the three digit number. The signed, 2s complement integers 
follow the unsigned integers, starting on row 256. This is possible because the look up table in the output module has
9 inputs --- the 8 bit number plus a single bit to signify if it is a signed integer or not, meaning it can index a 
total of 512 unique values (2^{9}). 

Rows 0 -- 255 contain the unsigned integers 0 -- 255
Rows 256 -- 383 contains the signed integers 0 -- 127
Rows 384 -- 511 contains tge signed integers -128 -- -1 
"""
# [begin-save_to_file]
with open("seven_segment_patterns_for_look_up_table.hex", "w") as hex_file:
    hex_file.write("v2.0 raw\n")
    hex_file.writelines(f"{hex(pattern)}\n" for pattern in unsigned_three_digit_patterns)
    hex_file.writelines(f"{hex(pattern)}\n" for pattern in signed_three_digit_patterns)
# [end-save_to_file]