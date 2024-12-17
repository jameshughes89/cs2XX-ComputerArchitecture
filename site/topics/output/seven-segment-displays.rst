**********************
Seven Segment Displays
**********************

* Binary values from the data bus have been readable through Digital's output components
* However, base 10 is preferable when viewing numbers
* Further, the data on the bus is always changing

    * Sometimes output should persist
    * Not all data on the bus needs to be output


* An output register will be used to improve system outputs
* Seven segment displays will be used as the mechanism for displaying base 10 numbers

.. figure:: real_seven_segment_display.png
    :width: 250 px
    :align: center
    :target: https://en.wikipedia.org/wiki/Seven-segment_display

    A common seven segment LED display. By turning different segments of the display on/off, different values can be
    visually represented.



Seven Segment Display
=====================



Binary Numbers to Decimal for a Seven Segment Displays
======================================================


Programmable Logic Array
------------------------


Look Up Table
-------------



Using a LUT to Map Numbers to Seven Segment Display Patterns
============================================================


* Since the system is 8 bit, the LUT will be used to decode an 8 bit number into the three digit output

.. figure:: lut_with_seven_segment_displays.png
    :width: 500 px
    :align: center

    Look up table for decoding an 8 bit binary number into a pattern for a seven segment display to represent a three
    digit decimal number. This design can display both unsigned and signed (two's complement) binary numbers, depending
    on the state of the "signed" signal. The left most seven segment display is only used to display a negative sign,
    when necessary. This image includes "probes" labelled -, 100s, 10s, and 1s for testing purposes, but are not
    necessary.


* The LUT takes 8 input lines representing an 8 bit number
* Additionally, the LUT will have one additional input line to signify if the number is signed

    * If the number is two's complement


* Thus, the LUT will have a total of 9 input signals

* The LUT would map these input signals to the corresponding seven segment display patterns for the output

    * For example, the number ``0b10101010`` would map to the patterns to display the decimal number 170
    * The number ``0b10101010`` would map to the pattern for -086 if the :math:`signed` signal was high


* Since each digit uses 8 bits to represent, and there are three digits, a total of 24 bits are needed
* However, there is an additional output signal needed to control the negative sign

    * Notice in the design that only one line from the LUT is connected to the left most seven segment display
    * Specifically, the line is connected directly to segment ``g`` of the display, which would be the negative sign


* Thus, there is a total of 25 output bits

* With the design used here

    * The least significant 8 bits of the 25 correspond to the least significant seven segment display
    * The most significant bit controls the negative sign


Creating Seven Segment Display Patterns
---------------------------------------

* A Python script will be used to generate the hex file to be loaded into the LUT
* A series of constants for each bit pattern will be created

    * Notice that these constants are added to a list
    * Within this list, the bit pattern for ``X`` is found in index ``X``


.. literalinclude:: create_seven_segment_patterns_for_look_up_table.py
    :language: python
    :lineno-match:
    :start-after: # [begin-seven_segment_digit_pattern_constants]
    :end-before: # [end-seven_segment_digit_pattern_constants]


* To create the 25 bit output patterns, two bitwise operators will be used

    * Bit shifting

        * Move bits to the left/right in a binary pattern
        * For example, consider shifting a binary pattern 4 bits to the left

            * ``0b1010 << 4`` results in ``0b10100000``


    * Bitwise ``OR``

        * Perform ``OR`` on each bit in two bit patterns
        * For example

            * ``0b11001100 | 0b11110000`` results in ``0b11111100``




Create the regular unsigned ints

    Mind the division

    bit shifting




Now create the 2s complement

Save the list to a file and load it up




For Next Time
=============

* Something?