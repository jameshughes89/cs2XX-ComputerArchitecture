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



Properties of Logical Operators
===============================

* There are several algebraic properties that hold for boolean logic
* Most of these are intuitive, but will be presented here for completness


.. list-table:: Boolean Algebra Laws
    :widths: auto
    :align: center

    * - Identity for :math:`\lor`
      - :math:`a \lor false = a`
    * - Identity for :math:`\land`
      - :math:`a \land true = a`
    * - Idempotence for :math:`\lor`
      - :math:`a \lor a = a`
    * - Idempotence for :math:`\land`
      - :math:`a \land a = a`
    * - Annihilator for :math:`\lor`
      - :math:`a \lor true = true`
    * - Annihilator for :math:`\land`
      - :math:`a \land false = false`
    * - Associativity of :math:`\lor`
      - :math:`a \lor (b \lor c) = (a \lor b) \lor c`
    * - Associativity of :math:`\land`
      - :math:`a \land (b \land c) = (a \land b) \land c`
    * - Commutativity of :math:`\lor`
      - :math:`a \lor b = b \lor a`
    * - Commutativity of :math:`\land`
      - :math:`a \land b = b \land a`
    * - Distributivity of :math:`\lor` over :math:`\land`
      - :math:`a \lor (b \land c) = (a \lor b) \land (a \lor c)`
    * - Distributivity of :math:`\land` over :math:`\lor`
      - :math:`a \land (b \land c) = (a \land b) \lor (a \land c)`
    * - Absorption 1
      - :math:`a \lor (a \land b) = a`
    * - Absorption 2
      - :math:`a \land (a \lor b) = a`



.. note::

    If the absorption laws are unclear, consider the corresponding distributive and idempotent laws. For example:

        :math:`a \lor (a \land b) = (a \lor a) \land (a \lor b) = a \land (a \lor b)`

    If :math:`a` is :math:`false`, given the :math:`\land` annihilator law, the expression evaluates to :math:`false`.

        :math:`false \land (false \lor b) = false`

    If :math:`a` is :math:`true`, given the :math:`\land` identity law, the expression evaluates to the result of
    :math:`(a \lor b)`, which, given the :math:`\lor` annihilator law, evaluates to :math:`true`, therefore, the whole
    expression evaluates to :math:`true`.

        :math:`true \land (true \lor b) = true \land true = true`





De Morgan's Law
---------------



For Next Time
=============

* `Watch Ben Eater's video on how transistors work <https://www.youtube.com/watch?v=DXvAlwMAxiA>`_
* Read Chapter 3 Sections 1 & 2 of your text

    * 7 pages