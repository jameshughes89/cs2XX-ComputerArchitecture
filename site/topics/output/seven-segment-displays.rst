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



Creating Seven Segment Display Patterns
=======================================

Create a script to write all combinations
Can load the script's output into the LUT

Want to have a signal for 2s complement or not
    Thus, we will have 8 inputs, plus 1 more for 2s complement mode
    or, 9 total

Three digits, so we need 1 byte for each, so, 3 bytes (24 bits)
plus one more bit for the sign
so, total of 25 bits

based on the configuration we will have, 8 least sig bits will be digit 1, etc.

    PICTURE?


To start, let's make constants
    Makes indexing easy

Create the regular unsigned ints

    Mind the division

    bit shifting




Now create the 2s complement

Save the list to a file and load it up




For Next Time
=============

* Something?