****************
Two's Complement
****************

* As long as enough bits are available, any positive integer (and zero) can be represented

    * With :math:`n` bits, the numbers :math:`0` through :math:`2^{n} - 1` can be represented
    * This would be an *unsigned* integer


* However, how can negative numbers be represented?



Sign Bit
========

* All binary numbers so far have been *unsigned*

    * They have only represented positive integers or zero


* Consider the following table with the number :math:`5` represented as an eight bit binary number

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    * - :math:`128`
      - :math:`64`
      - :math:`32`
      - :math:`16`
      - :math:`8`
      - :math:`4`
      - :math:`2`
      - :math:`1`
    * - ``0``
      - ``0``
      - ``0``
      - ``0``
      - ``0``
      - ``1``
      - ``0``
      - ``1``


* To determine what number this represents, add the place value of each bit that is ``1``
* In the above example, the bits representing the value :math:`4` and :math:`1` are ``1``, thus the number is :math:`5`

    * :math:`4 + 1 = 5`


* :doc:`As discussed in an earlier topic, this works the same way with base ten numbers </topics/numbers/number-bases>`
* Addition in binary also works the same as base ten, but with only two symbols

    * Add up the values in each position, and carry to the next significant position if needed


.. list-table::
    :widths: auto
    :align: center

    * - **Carry**
      -
      -
      - ``1``
      - ``1``
      -
      -
      -
      -
      -
      - :math:`1`
      -
      -
    * - **Number 1**
      - ``0``
      - ``1``
      - ``0``
      - ``1``
      - ``1``
      - ``1``
      - ``0``
      - ``0``
      -
      -
      - :math:`9`
      - :math:`2`
    * - **Number 2**
      - ``1``
      - ``0``
      - ``0``
      - ``1``
      - ``1``
      - ``0``
      - ``1``
      - ``0``
      -
      - :math:`1`
      - :math:`5`
      - :math:`4`
    * - **Sum**
      - ``1``
      - ``1``
      - ``1``
      - ``1``
      - ``0``
      - ``1``
      - ``1``
      - ``0``
      -
      - :math:`2`
      - :math:`4`
      - :math:`6`


* The above table shows addition of two numbers, in binary and decimal

    * The left side is binary addition, the right side is decimal


* A simple way to represent negative numbers is to use the most significant bit as a sign bit
* Consider the number :math:`5` --- ``00000101``
* To represent :math:`-5`, replace the most significant bit (left most) with a ``1`` --- ``10000101``

    * With this strategy, ``10000101`` would be :math:`-5`, not :math:`133`


* Since the most significant bit is used as a sign, fewer positive numbers can be represented

    * But negative numbers are now possible


* Below is a table showing all the possible values a four bit binary number can represent with the use of a sign bit

.. list-table:: All four bit values representable with the use of a sign bit
    :widths: auto
    :align: center

    * - ``1111``
      - :math:`-7`
    * - ``1110``
      - :math:`-6`
    * - ``1101``
      - :math:`-5`
    * - ``1100``
      - :math:`-4`
    * - ``1011``
      - :math:`-3`
    * - ``1010``
      - :math:`-2`
    * - ``1001``
      - :math:`-1`
    * - ``1000``
      - :math:`-0`
    * - ``0000``
      - :math:`0`
    * - ``0001``
      - :math:`1`
    * - ``0010``
      - :math:`2`
    * - ``0011``
      - :math:`3`
    * - ``0100``
      - :math:`4`
    * - ``0101``
      - :math:`5`
    * - ``0110``
      - :math:`6`
    * - ``0111``
      - :math:`7`



Problems and Limitations
------------------------

* One may have started to notice some issues with this strategy
* First, there are two patterns that represent the number :math:`0`

    * ``1000`` meaning :math:`-0`
    * ``0000`` meaning :math:`0`
    * Although one is negative, this does not have any meaning for integers


* Another issue is that the pattern for the numbers change depending on the number of bits
* With positive numbers, this is not a problem

    * ``0101`` is the same as ``00000101``
    * They both represent :math:`5`

* But consider the four bit binary number ``1101`` and the eight bit number ``10000101``

    * Both represent the number :math:`-5`, yet they have different patterns


* And finally, another issue is addition
* With decimal numbers, adding a negative number is the same as subtraction

    * :math:`5 + -5 = 0`


* If one were to try to add a negative number with a sign bit, it will not work properly 

.. list-table:: Adding a negative binary number with a sign bit
    :widths: auto
    :align: center

    * - **Carry**
      - ``1``
      - ``1``
      -
      - ``1``
      -
      -
      -
    * - **Number 1**
      -
      - ``0``
      - ``1``
      - ``0``
      - ``1``
      -
      - :math:`5`
    * - **Number 2**
      -
      - ``1``
      - ``1``
      - ``0``
      - ``1``
      -
      - :math:`-5`
    * - **Sum**
      - ``1``
      - ``0``
      - ``0``
      - ``1``
      - ``0``
      -
      - :math:`2?`


* Even if one ignores the fact that the sign bit got carried to a fifth bit, the arithmetic does not work out




One's Compliment
================



Two's Compliment
================



For Next Time
=============

* Something?