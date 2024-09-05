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




no way to do negative numbers

use most significant bit as the sign bit
show 5 example

show whole table of all 4/3 bit numbers

problems/limitations are:
1. need to know how many bits there are/what the most significant bit is
    8 bit -5 vs 4 bit -5

2. Two 0s, which is weird

3. Addition is weird



One's Compliment
================



Two's Compliment
================



For Next Time
=============

* Something?