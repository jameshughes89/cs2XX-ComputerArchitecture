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

* A system to convert the binary numbers to their respective seven segment display patterns needs to be developed
* As discussed, a single byte can be used for each seven segment display
* Here, the display's ``a`` input will be the least significant bit, and ``h`` will be the most significant

    * This ordering is a design decision and not a requirement


* Below is a table showing each decimal number's bit pattern for the seven segment display

.. list-table:: Decimal Numbers and Their Seven Segment Display Patterns following ``hgfedcba``
    :widths: auto

    * - Decimal
      - Binary
      -
      - Display Pattern
      - Display Hex
      - Output
    * - ``0``
      - ``0b00000000``
      -
      - ``0b00111111``
      - ``0x3F``
      - .. image:: seven_segment_display_0.png
            :width: 50
    * - ``1``
      - ``0b00000001``
      -
      - ``0b00000110``
      - ``0x06``
      - .. image:: seven_segment_display_1.png
            :width: 50
    * - ``2``
      - ``0b00000010``
      -
      - ``0b01011011``
      - ``0x5B``
      - .. image:: seven_segment_display_2.png
            :width: 50
    * - ``3``
      - ``0b00000011``
      -
      - ``0b01001111``
      - ``0x4F``
      - .. image:: seven_segment_display_3.png
            :width: 50
    * - ``4``
      - ``0b00000100``
      -
      - ``0b01100110``
      - ``0x66``
      - .. image:: seven_segment_display_4.png
            :width: 50
    * - ``5``
      - ``0b00000101``
      -
      - ``0b01101101``
      - ``0x6D``
      - .. image:: seven_segment_display_5.png
            :width: 50
    * - ``6``
      - ``0b00000110``
      -
      - ``0b01111101``
      - ``0x7D``
      - .. image:: seven_segment_display_6.png
            :width: 50
    * - ``7``
      - ``0b00000111``
      -
      - ``0b00000111``
      - ``0x07``
      - .. image:: seven_segment_display_7.png
            :width: 50
    * - ``8``
      - ``0b00001000``
      -
      - ``0b01111111``
      - ``0x7F``
      - .. image:: seven_segment_display_8.png
            :width: 50
    * - ``9``
      - ``0b00001001``
      -
      - ``0b01101111``
      - ``0x6F``
      - .. image:: seven_segment_display_9.png
            :width: 50

.. note::

    One may have noticed that the **seven** segment display pattern for the number **seven** is the binary number **seven**.

    This is in no way meaningful, and is a consequence of the arbitrary bit ordering to the inputs, but an interesting
    observation nonetheless.


* Consider, however, the number 10, which is easily representable in binary with 8 bits
* One cannot represent this number with a single digit

    * Although hexadecimal can be used, and an ``A`` can be displayed on a seven segment display, this misses the point
    * The goal is to show decimal numerals
    * And further, the same issue arises with hexadecimal numbers once the number 16 is hit


* The system being designed can represent eight bit numbers

    * A total of 256
    * 0 -- 255


* Thus, a total of three digits are required for this system's output

* Fortunately, there is a simple way to deal with this
* Use three displays and three bytes for an 8 bit integer

    * Map a single 8 bit integer to three 8 bit patterns, one for each of the three displays


* In other words, the number 10 maps to a byte for 0, a byte for 1, and another byte for 0

    * ``0b00001010`` maps to ``0b0011111111``, ``0b00000110``, and ``0b0011111111``


* Below is an example of displaying the number 123

    * ``0b01111011`` maps to ``0b00000110``, ``0b01011011``, and ``0b01001111``


.. figure:: seven_segment_display_123.png
    :width: 250 px
    :align: center

    Three seven segment displays showing the number 123. The number 123, represented in binary as ``0b01111011`` must
    map to three bytes to display 1, 2, and 3. These bytes would be ``0b00000110``, ``0b01011011``, and ``0b01001111``
    respectively.


* Further, since the system works with two's complement numbers, negative numbers should be displayable on the output

    * Numbers -128 -- 127


* This is achieved with a forth display that would only ever activate the ``g`` input, when necessary

    * This forth, leftmost display would only activate ``g`` when showing a negative number
    * Positive numbers would have nothing displayed on this forth display


.. figure:: seven_segment_display_-123.png
    :width: 333 px
    :align: center

    Four seven segment displays showing the twos complement number -123 (``0b10000101``). The left most display in this
    configuration would only ever be used to show the negative sign, when appropriate.





Programmable Logic Array
------------------------


Look Up Table
-------------



Creating Seven Segment Display Patterns
=======================================



For Next Time
=============

* Something?