************
Truth Tables
************

* Much of the following will likely be a review of already well understood concepts
* This content is covered for completeness, but will be kept at a relatively high level



Boolean Logic
=============

* Boolean logic is a form of algebra that operates on boolean values that can take on only two states
* These states are typically called *True* and *False*

    * Depending on context, these are sometimes referred to as *On*/*Off*, ``1``/``0``, or *high voltage*/*low voltage*


* Within the algebra, the *operands* are values that take on one of these two states
* The *operators* act on these operands to produce a new boolean value


.. note::

    If this terminology is throwing you off, remember that this is like the integer operators/operands you are familiar
    with. Consider the expression :math:`1 + 2`. The operands here are integers :math:`1` and :math:`2` and the operator
    is :math:`+`, which means addition. Here, addition is an operator that takes two integer values and produces a new
    integer value.

    With boolean logic, the operands can have one of two boolean values as opposed to an infinite number, like with
    integers, and the operators will take two boolean values to produce a new boolean value.



* There are three basic boolean operators

    * **Not**

        * Unary operator --- only operates on a single operand to produce a single value
        * Given some boolean value :math:`a`, invert it

            * In other words, if :math:`a` is *True*, not :math:`a` is *False*, and *vice versa*


        * Typically denoted as :math:`\lnot a` or sometimes :math:`\overline a`


    * **And**

        * Binary operator --- operates on two operands to produce a single value
        * Given boolean values :math:`a` and :math:`b`, return *True* if both values are *True*, *False* otherwise
        * Denoted as :math:`a \land b`


    * **Or**

        * Binary operator --- operates on two operands to produce a single value
        * Given boolean values :math:`a` and :math:`b`, return *True* if both or either are *True*, *False* otherwise
        * Denoted as :math:`a \lor b`




* NOR
* NAND
* EXOR
* XNOR


* Show the syntax too



Truth Tables
============



Properties of Logical Operators
===============================


De Morgan's Law
---------------



For Next Time
=============

* `Watch Ben Eater's video on how transistors work <https://www.youtube.com/watch?v=DXvAlwMAxiA>`_
* Read Chapter 3 Sections 1 & 2 of your text

    * 7 pages