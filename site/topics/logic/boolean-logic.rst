*************
Boolean Logic
*************

* Much of the following will likely be a review of already well understood concepts
* This content is covered for completeness, but will be kept at a relatively high level



Boolean Operators and Operands
==============================

* Boolean logic is a form of algebra that operates on boolean values that can take on only two states
* These states are typically called *true* and *false*

    * Depending on context, these are sometimes referred to as *On*/*Off*, ``1``/``0``, or *high voltage*/*low voltage*


* Within the algebra, the *operands* are values that take on one of these two states
* The *operators* act on these operands to produce a new boolean value


.. note::

    If this terminology is throwing you off, remember that this is like the integer operators/operands you are familiar
    with. Consider the expression :math:`1 + 2`. The operands here are integers :math:`1` and :math:`2` and the operator
    is :math:`+`, which means addition. Here, addition is an operator that takes two integer values and produces a new
    integer value.



* There are three basic boolean operators

    * **Not**

        * Unary operator --- only operates on a single operand to produce a single value
        * Given some boolean value :math:`a`, invert it

            * In other words, if :math:`a` is *true*, not :math:`a` is *false*, and *vice versa*


        * Typically denoted as :math:`\lnot a` or sometimes :math:`\overline a`


    * **And**

        * Binary operator --- operates on two operands to produce a single value
        * Given boolean values :math:`a` and :math:`b`, return *true* if both values are *true*, *false* otherwise
        * Denoted as :math:`a \land b`


    * **Or**

        * Binary operator --- operates on two operands to produce a single value
        * Given boolean values :math:`a` and :math:`b`, return *true* if both or either are *true*, *false* otherwise
        * Denoted as :math:`a \lor b`


* There are additional boolean operators that can be made up from the three basic operators
* Three of these are commonly used within the context of computer architecture, thus they will be presented here

    * **Exclusive Or** (**XOR**)

        * Binary operator --- operates on two operands to produce a single value
        * Given boolean values :math:`a` and :math:`b`, return *true* if and only if either are *true*, *false* otherwise

            * Similar to or, but if both are *true*, it returns *false*

        * Denoted as :math:`a \oplus b`
        * Equivalent to :math:`(a \lor b) \land \lnot (a \land b)`


    * **Not Or** (**NOR**)

        * Literally *not or*
        * Sometimes denoted as :math:`\overline \lor`
        * Equivalent to :math:`\lnot (a \lor b)`
        * Functionally complete --- can be used to generate all other boolean operators


    * **Not And** (**NAND**)

        * Literally *not and*
        * Sometimes denoted as :math:`\overline \land`
        * Equivalent to :math:`\lnot (a \land b)`
        * Functionally complete --- can be used to generate all other boolean operators



Truth Tables
============

* Truth tables provide a structured visualization of all possible truth values for logical expressions
* These are probably best understood with examples
* Below is a truth table for the above boolean operators for all possible combinations of values for two operands


.. list-table:: Truth Table for Basic and Common Logical Operators
    :widths: auto
    :align: center
    :header-rows: 1

    * - :math:`a`
      - :math:`b`
      -
      - :math:`\lnot a`
      - :math:`a \land b`
      - :math:`a \lor b`
      -
      - :math:`a \oplus b`
      - :math:`\lnot (a \land b)`
      - :math:`\lnot (a \lor b)`
    * - :math:`false`
      - :math:`false`
      -
      - :math:`true`
      - :math:`false`
      - :math:`false`
      -
      - :math:`false`
      - :math:`true`
      - :math:`true`
    * - :math:`false`
      - :math:`true`
      -
      - :math:`true`
      - :math:`false`
      - :math:`true`
      -
      - :math:`true`
      - :math:`true`
      - :math:`false`
    * - :math:`true`
      - :math:`false`
      -
      - :math:`false`
      - :math:`false`
      - :math:`true`
      -
      - :math:`true`
      - :math:`true`
      - :math:`false`
    * - :math:`true`
      - :math:`true`
      -
      - :math:`false`
      - :math:`true`
      - :math:`true`
      -
      - :math:`false`
      - :math:`false`
      - :math:`false`



* In the context of digital circuits, it is common to use ``0`` and ``1`` in place of :math:`false` and :math:`true`
* Going forward, ``0`` and ``1`` will be used for thouse course


.. note::

    The empty columns do not have any formal meaning. They are included here for visual clarity.



Building Out the Truth Table
----------------------------

* Notice the :math:`\lnot (a \land b)` and :math:`\lnot (a \lor b)` columns in the truth tables are compound operations

    * They are made up of two operations --- **not** and **and/or**


* These columns are the inverse of the basic and/or columns in the table

    * Literally **not** the result of those columns


* Consider a more complex compound expression --- :math:`(a \land \lnot b) \lor \lnot c`
* It is often helpful to break the operation down into parts that are easier to calculate
* Then, build out a truth table to solve each part individually

.. list-table:: Truth Table for :math:`(a \land \lnot b) \lor \lnot c`
    :widths: auto
    :align: center
    :header-rows: 1

    * - :math:`a`
      - :math:`b`
      - :math:`c`
      -
      - :math:`\lnot b`
      - :math:`\lnot c`
      -
      - :math:`a \land \lnot b`
      -
      - :math:`(a \land \lnot b) \lor \lnot c`
    * - ``0``
      - ``0``
      - ``0``
      -
      - ``1``
      - ``1``
      -
      - ``0``
      -
      - ``1``
    * - ``0``
      - ``0``
      - ``1``
      -
      - ``1``
      - ``0``
      -
      - ``0``
      -
      - ``0``
    * - ``0``
      - ``1``
      - ``0``
      -
      - ``0``
      - ``1``
      -
      - ``0``
      -
      - ``1``
    * - ``0``
      - ``1``
      - ``1``
      -
      - ``0``
      - ``0``
      -
      - ``0``
      -
      - ``0``
    * - ``1``
      - ``0``
      - ``0``
      -
      - ``1``
      - ``1``
      -
      - ``1``
      -
      - ``1``
    * - ``1``
      - ``0``
      - ``1``
      -
      - ``1``
      - ``0``
      -
      - ``1``
      -
      - ``1``
    * - ``1``
      - ``1``
      - ``0``
      -
      - ``0``
      - ``1``
      -
      - ``0``
      -
      - ``1``
    * - ``1``
      - ``1``
      - ``1``
      -
      - ``0``
      - ``0``
      -
      - ``0``
      -
      - ``0``


.. admonition:: Activity

    Create and complete a truth table for the boolean expression :math:`\lnot(a \land b) \lor (a \land \lnot b)`.

    .. list-table::
        :widths: auto
        :align: center
        :header-rows: 1

        * - :math:`a`
          - :math:`b`
          -
          - :math:`\lnot b`
          - :math:`a \land b`
          -
          - :math:`a \land \lnot b`
          - :math:`\lnot(a \land b)`
          -
          - :math:`\lnot(a \land b) \lor (a \land \lnot b)`
        * -
          -
          -
          -
          -
          -
          -
          -
          -
          -
        * -
          -
          -
          -
          -
          -
          -
          -
          -
          -
        * -
          -
          -
          -
          -
          -
          -
          -
          -
          -
        * -
          -
          -
          -
          -
          -
          -
          -
          -
          -


Properties of Logical Operators
===============================


De Morgan's Law
---------------



For Next Time
=============

* `Watch Ben Eater's video on how transistors work <https://www.youtube.com/watch?v=DXvAlwMAxiA>`_
* Read Chapter 3 Sections 1 & 2 of your text

    * 7 pages