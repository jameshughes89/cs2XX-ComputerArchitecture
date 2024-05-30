************
Number Bases
************



Decimal (Base Ten)
==================

* The decimal number system is used in everyday life
* The decimal number system is base ten; it consists of ten different symbols/numerals

    * :math:`0, 1, 2, 3, 4, 5, 6, 7, 8, 9`


* These symbols have an ordering to them

    * :math:`0 \rightarrow 1 \rightarrow  2 \rightarrow  3 \rightarrow  4 \rightarrow  5 \rightarrow  6 \rightarrow  7 \rightarrow  8 \rightarrow  9`


* These symbols also have a meaning/value associated with them

    * The symbol :math:`5` means *five*
    * It conveys a magnitude


* The magnitude of these values correspond to the ordering

    * :math:`0 < 1 <  2 <  3 <  4 <  5 <  6 <  7 <  8 <  9`



Counting in Base Ten
--------------------

* Counting in base ten consists of moving to the next symbol

    .. list-table:: Counting with Ten Symbols
        :widths: 50 50

        * - :math:`0`
          - Zero
        * - :math:`1`
          - One
        * - :math:`2`
          - Two
        * - :math:`3`
          - Three
        * - :math:`4`
          - Four
        * - :math:`5`
          - Five
        * - :math:`6`
          - Six
        * - :math:`7`
          - Seven
        * - :math:`8`
          - Eight
        * - :math:`9`
          - Nine
        * - :math:`????`
          - Ten?


* However, there are only ten unique symbols
* This means it's not possible to count past nine with the symbols alone
* This is where symbol position comes in


Position
^^^^^^^^

* First, consider that each number has an infinite number of zeros in front of it

    * Why this is will be discussed shortly


* Consider the below table where only seven of the leading zeros are included

    * Thus, these numbers will each have a total of eight symbols
    * Each of these symbols/numerals, in this context, is called a *digit*

        * Digit comes from latin (*digitus*), meaning finger or toe, of which, humans typically have ten of each


    .. list-table:: Values Expressed with Eight Digits
        :widths: 50 50

        * - :math:`00000000`
          - Zero
        * - :math:`00000001`
          - One
        * - :math:`00000002`
          - Two
        * - :math:`00000003`
          - Three
        * - :math:`00000004`
          - Four
        * - :math:`00000005`
          - Five
        * - :math:`00000006`
          - Six
        * - :math:`00000007`
          - Seven
        * - :math:`00000008`
          - Eight
        * - :math:`00000009`
          - Nine


* To count past the value nine, a new rule is introduced
* If the no more symbols are left

    * Reset the symbol to zero in the current position
    * Change to the subsequent symbol in the next position


    .. list-table:: Counting with Digits
        :widths: 50 50

        * - ...
          - ...
        * - :math:`00000008`
          - Eight
        * - :math:`00000009`
          - Nine
        * - :math:`00000010`
          - Ten
        * - :math:`00000011`
          - Eleven
        * - ...
          - ...
        * - :math:`00000018`
          - Eighteen
        * - :math:`00000019`
          - Nineteen
        * - :math:`00000020`
          - Twenty
        * - ...
          - ...
        * - :math:`00000099`
          - Ninety Nine
        * - :math:`00000100`
          - One Hundred
        * - :math:`00000101`
          - One Hundred and One
        * - ...
          - ...


* Consider the number :math:`101`
* Although this number contains two ones, they have a different meaning because of their position


Names
^^^^^

* Each of these positions has a name
* From left to right, they are

    .. list-table:: Digit Position Names
        :widths: 50 50 50 50

        * - First Digit
          - Ones
          - :math:`10^{0}`
          - :math:`1`
        * - Second Digit
          - Tens
          - :math:`10^{1}`
          - :math:`10`
        * - Third Digit
          - Hundreds
          - :math:`10^{2}`
          - :math:`100`
        * - Fourth Digit
          - Thousands
          - :math:`10^{3}`
          - :math:`1000`
        * - Fifth Digit
          - Ten Thousands
          - :math:`10^{4}`
          - :math:`10000`
        * - Sixth Digit
          - Hundred Thousands
          - :math:`10^{5}`
          - :math:`100000`
        * - Seventh Digit
          - Millions
          - :math:`10^{6}`
          - :math:`1000000`
        * - Eighth Digit
          - Ten Millions
          - :math:`10^{7}`
          - :math:`10000000`
        * - ...
          - ...
          - ...
          - ...


* As a consequence of the counting pattern, each position corresponds to a value that is the base raised to some power
* Consider the number :math:`123`
* The symbol :math:`1` in the hundreds position is :math:`1 \times 10^{2}`

    * There is one *hundred*


* The symbol :math:`2` in the tens position is :math:`2 \times 10^{1}`

    * There are two *tens*


* The symbol :math:`3` in the ones position is :math:`3 \times 10^{0}`

    * Three *ones*


* Thus, the number is :math:`1 \times 10^{2} + 2 \times 10^{1} + 3 \times 10^{0}`


* It may feel strange to think about the number :math:`123` like this
* But this is what the decimal encoding of the number is conveying

.. figure:: 123_with_cash.png
    :width: 500 px
    :align: center
    :target: https://en.wikipedia.org/wiki/Canadian_dollar

    The value :math:`123` represented with Canadian Dollars. There is one hundred, two tens, and three ones.


Consequence of Finite Digits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Although with integers, there are an infinite number of leading zeros and positions
* Only eight digits were used to encode the numbers in the above examples
* Ths means there is a limit to the number of unique positive integer values that can be expressed
* The largest number is :math:`99999999`

    * Ninety nine million, nine hundred and ninety nine thousand, nine hundred and ninety nine


* Obviously there are values larger than this, but they are not representable with only 8 digits



Binary (Base Two)
=================

* Decimal is the typical way numbers are encoded in every day life
* However, base ten (decimal) is only an encoding

    * It's not a *number*, it's a way to represent a number


* Other bases could just as easily be used
* For example, binary (base two)
* Instead of ten symbols, only two are used --- :math:`0, 1`

    * :math:`0` means zero, like base ten
    * :math:`1` means one, like base ten


* The symbols have an ordering to the magnitude of values, like base ten

    * :math:`0 \rightarrow 1`
    * :math:`0 < 1`


* Position matters, like base ten

    * The value of a :math:`1` depends on *where* it is


* There are an infinite number of leading zeros

    * :math:`1 == 00000001 == 0000000000000001`


* In decimal, the symbols are called digits
* In binary, they are called *bits*

    * Binary information digit --- bit


* The counting rules are the same

    * Increment to the next symbol
    * If there are no more symbols

        * Reset to :math:`0`
        * Increment the symbol in the next position


    .. list-table:: Counting in Binary
        :widths: 50 50

        * - :math:`00000000`
          - Zero
        * - :math:`00000001`
          - One
        * - :math:`00000010`
          - Two
        * - :math:`00000011`
          - Three
        * - :math:`00000100`
          - Four
        * - :math:`00000101`
          - Five
        * - :math:`00000110`
          - Six
        * - :math:`00000111`
          - Seven
        * - :math:`00001000`
          - Eight
        * - ...
          - ...


* With eight bits, the largest positive integer that could be represented is :math:`255`

    * Can represent the numbers 0 through to 255


* Like base ten, the specific bit position carries different values
* These values are always the base to some power
* Although these bit positions don't really go by specific names, they can be named like the digits

    .. list-table:: Bit Position Names
        :widths: 50 50 50 50

        * - First Digit
          - Ones
          - :math:`2^{0}`
          - :math:`1`
        * - Second Digit
          - Twos
          - :math:`2^{1}`
          - :math:`2`
        * - Third Digit
          - Fours
          - :math:`2^{2}`
          - :math:`4`
        * - Fourth Digit
          - Eights
          - :math:`2^{3}`
          - :math:`8`
        * - Fifth Digit
          - Sixteens
          - :math:`2^{4}`
          - :math:`16`
        * - Sixth Digit
          - Thirty-twos
          - :math:`2^{5}`
          - :math:`32`
        * - Seventh Digit
          - Sixty-fours
          - :math:`2^{6}`
          - :math:`62`
        * - Eighth Digit
          - One hundred and twenty eights
          - :math:`2^{7}`
          - :math:`128`
        * - ...
          - ...
          - ...
          - ...


* Like base ten, the binary number can be broken down to the sum of its positional values
* Consider the number :math:`1111011`

    * One *Sixty-four*
    * One *thirty-two*
    * One *sixteen*
    * One *eight*
    * Zero *fours*
    * One *two*
    * One *one*


* Thus, the number is

    :math:`1 \times 2^{6} + 1 \times 2^{5} + 1 \times 2^{4} + 1 \times 2^{3} + 0 \times 2^{2} + 1 \times 2^{1} + 1 \times 2^{0}`

    :math:`1 \times 64 + 1 \times 32 + 1 \times 16 + 1 \times 8 + 0 \times 4 + 1 \times 2 + 1 \times 1`

    :math:`64 + 32 + 16 + 8 + 2 + 1`

    :math:`123`


.. note::

    Position really matters --- have you ever counted to :math:`31` on one hand?

    Typically, when counting with fingers, the position of the finger is ignored. This means that the biggest number
    one could count to on one hand is five.

    However, it is possible to make use of the position of each finger to get more out of your hand. Try it yourself.

    .. figure:: finger_counting_binary_19.png
        :width: 150 px
        :align: center
        :target: https://en.wikipedia.org/wiki/Finger_binary

        The number 19 in binary represented with fingers. The thumb is the least significant bit (ones) and the pinky
        finger is the most significant bit (sixteens).



Hexadecimal (Base 16)
=====================



Converting Numbers Between Bases
================================



*Meaning*
=========



For Next Time
=============

* Get your computer at home :doc:`set up for the course </getting-set/getting-set>`
* Read Chapter 1 of your text

    * 19 pages


* Read Chapter 2 of your text

    * 23 pages