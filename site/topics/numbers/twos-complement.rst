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

* A potential alternative to using a sign bit is *ones complement*
* The strategy is similar to a sign bit, but with ones complement, all bits are flipped for negative numbers

    * Take the *complement* of each bit

.. list-table:: All four bit values representable with the ones complement
    :widths: auto
    :align: center

    * - ``1000``
      - :math:`-7`
    * - ``1001``
      - :math:`-6`
    * - ``1010``
      - :math:`-5`
    * - ``1011``
      - :math:`-4`
    * - ``1100``
      - :math:`-3`
    * - ``1101``
      - :math:`-2`
    * - ``1110``
      - :math:`-1`
    * - ``1111``
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


* Like with a sign bit, it is simple to identify negative numbers by looking for a ``1`` in the most significant bit

* But the issue of the pattern for negative numbers changing depending on the number of bits is *somewhat* resolved
* Consider the number :math:`-3`

    * With three bits, :math:`-3` is represented as ``100``
    * With four bits, :math:`-3` is represented as ``1100``

* Although the pattern is different, the idea is that negative numbers have an infinite number of leading ``1``\s

    * As opposed to an infinite number of ``0``\s as with positive numbers


Problems and Limitations
------------------------

* Unfortunately, ones complement still has the oddity of having two patterns for the number :math:`0`

    * ``0000`` for :math:`0`
    * ``1111`` for :math:`-0`


* Further, addition with negative numbers is still not perfect


.. list-table:: Adding a negative binary number with ones complement
    :widths: auto
    :align: center

    * - **Carry**
      -
      -
      -
      -
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
      - ``0``
      - ``1``
      - ``0``
      -
      - :math:`-5`
    * - **Sum**
      -
      - ``1``
      - ``1``
      - ``1``
      - ``1``
      -
      - :math:`-0`


* The above example results in a correct addition, but issues arise with non zero results

.. note::

    With binary addition and a fixed number of bits, any carry that results in an overflow will ultimately be ignored.
    For example, consider the four bit addition of ``1111`` (:math:`7`) + ``0001`` (:math:`1`). The result is clearly
    ``10000`` (:math:`8`), but since there are only four bits available, the overflowed value is lost, and the result
    would be ``0000``.


.. list-table:: Adding a negative binary number with ones complement
    :widths: auto
    :align: center

    * - **Carry**
      -
      - ``1``
      -
      -
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
      - ``0``
      -
      - :math:`-3`
    * - **Sum**
      -  (ignore overflow) ``1``
      - ``0``
      - ``0``
      - ``0``
      - ``1``
      -
      - :math:`1?`


.. list-table:: Adding a negative binary number with ones complement
    :widths: auto
    :align: center

    * - **Carry**
      -
      - ``1``
      -
      -
      -
      -
      -
    * - **Number 1**
      -
      - ``1``
      - ``1``
      - ``0``
      - ``1``
      -
      - :math:`-2`
    * - **Number 2**
      -
      - ``0``
      - ``1``
      - ``1``
      - ``0``
      -
      - :math:`6`
    * - **Sum**
      -  (ignore overflow) ``1``
      - ``0``
      - ``0``
      - ``1``
      - ``1``
      -
      - :math:`3?`


.. list-table:: Adding a negative binary number with ones complement
    :widths: auto
    :align: center

    * - **Carry**
      -
      - ``1``
      - ``1``
      - ``1``
      -
      -
      -
    * - **Number 1**
      -
      - ``1``
      - ``0``
      - ``1``
      - ``1``
      -
      - :math:`-4`
    * - **Number 2**
      -
      - ``1``
      - ``1``
      - ``0``
      - ``1``
      -
      - :math:`-2`
    * - **Sum**
      -  (ignore overflow) ``1``
      - ``1``
      - ``0``
      - ``0``
      - ``0``
      -
      - :math:`-7?`


* The fact that the overflow value is lost is important for addition of negative numbers to work
* However, when looking at these results, it is clear that addition with negative numbers doesn't quite work
* Except for when the sum is :math:`0`, all results are one less than what they should be
* In fact, considering :math:`-0` is a strange number, maybe the sum should be :math:`0`, which is also off by one

    * Refer to the table of four bit ones complement binary numbers to make this more clear
    * Notice how each sum is one row above where the sum should be



Two's Compliment
================



For Next Time
=============

* Something?