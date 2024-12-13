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

* Seven segment displays are made up of seven toggleable segments
* By turning these segments on/off, different symbols can be represented

    * A total of :math:`2^{7}` (:math:`128`) unique patterns can be represented

        * Although not all would necessary be meaningful


.. figure:: seven_segment_display_labelled.png
    :width: 200 px
    :align: center

    A seven segment display from Digital with the eight inputs and corresponding segments labelled. When a high signal
    is applied to an input, the respective segment would turn on.


* Although they are called seven segment displays, it's common to have an eighth segment representing a decimal point

    * Which explains why these components have eight inputs
    * Thus, there is actually a total of :math:`2^{8}` (:math:`256`) unique patterns


* Since a one signal controls one segment, eight signals are required to control the eight total segments

.. figure:: seven_segment_display.gif
    :width: 200 px
    :align: center

    Animation of each of the eight inputs on a seven segment display being activated. As each input is made high, the
    corresponding segment turns on.


* One can think of these eight signals as 8 bits/1 byte
* But, it is important to remember that the bit patterns is an encoding

    * Some decoding is needed to derive meaning


* For example, assume a byte is used to control the seven segment display such that ``a`` is the least significant bit

    * Each bit in the byte controls one segment
    * ``hgfedcba``


* The number 9 is ``0b00001001``
* However, this bit pattern would display the following

.. figure:: seven_segment_display_00001001.png
    :width: 333 px
    :align: center

    The state of a seven segment display when the inputs are set to ``0b00001001``, ordered such that ``a`` is the least
    significant bit and ``h`` is the most significant.


* In other words, the byte representing 9 as an integer has an entirely different meaning when used for the display

    * ``0b00001001`` is only an encoding



Binary Numbers to Decimal for a Seven Segment Displays
======================================================


Programmable Logic Array
------------------------


Look Up Table
-------------



Creating Seven Segment Display Patterns
=======================================



For Next Time
=============

* Something?