***********
Basic Gates
***********

* Feel free to use your laptop
* You are strongly encourage to work with others

    * When you get stuck, ask those sitting around you for help
    * Get used to working together in the labs
    * Peer teaching and peer learning has been empirically shown to be very effective


For these questions, feel free to use a single Digital workspace for all the circuits. However, label each circuit with
labelled rectangles. These are components that can be found under "Components -> Misc. -> Decoration -> Rectangle".

Where possible, each question should have complete tests. The test component can be found under "Components -> Misc. ->
Test case". Once a test component is placed on the workspace, right click on the component to edit the test data.

Questions may have restrictions on the logic gates that may be used. When restrictions are stated, they only apply to
the gates; inputs, outputs, wires, etc. may be still be used.



Creating Gates with Universal Operators
=======================================

For these questions, although only a single gate type may be used, feel free to use as many copies of these gates as
needed.


``NAND``
--------

#. Using only ``NAND``, create a circuit that performs ``NAND``

    * This circuit is intentionally trivial


#. Using only ``NAND``, create a circuit that performs ``NOT``
#. Using only ``NAND`` and ``NOT``, perform ``AND``
#. Using only ``NAND`` and ``NOT``, perform ``OR``
#. Using only ``NAND`` and ``NOT``, perform ``NOR``


``NOR``
-------

#. Using only ``NOR``, create a circuit that performs ``NOR``

        * This circuit is intentionally trivial


#. Using only ``NOR``, create a circuit that performs ``NOT``
#. Using only ``NOR`` and ``NOT``, perform ``OR``
#. Using only ``NOR`` and ``NOT``, perform ``AND``
#. Using only ``NOR`` and ``NOT``, perform ``NAND``



From Truth Tables
=================

For these questions, first create the truth table if one is not already provided.


#. Using **at least** one ``NOT``, create a circuit that performs the following

    .. list-table::
        :widths: auto
        :header-rows: 1

        * - :math:`A`
          -
          - :math:`O`
        * - ``0``
          -
          - ``0``
        * - ``1``
          -
          - ``1``


#. Using only ``OR`` and ``NOT``, create a circuit that always outputs ``1``, regardless of the input

    .. list-table::
        :widths: auto
        :header-rows: 1

        * - :math:`A`
          -
          - :math:`O`
        * - ``0``
          -
          - ``1``
        * - ``1``
          -
          - ``1``


#. Using only ``AND`` and ``NOT``, create a circuit that always outputs ``0``, regardless of the input

    .. list-table::
        :widths: auto
        :header-rows: 1

        * - :math:`A`
          -
          - :math:`O`
        * - ``0``
          -
          - ``0``
        * - ``1``
          -
          - ``0``


#. Using only ``AND``, ``OR``, and ``NOT``, create a circuit that performs ``XOR``
#. Using only a single ``AND`` and a single ``OR``, create a circuit that performs :math:`(a \lor b) \land (a \lor c)`
#. Using only a single ``AND`` and a single ``OR``, create a circuit that performs the following

    .. list-table::
        :widths: auto
        :header-rows: 1

        * - :math:`A`
          -
          - :math:`O`
        * - ``0``
          -
          - ``0``
        * - ``1``
          -
          - ``1``


#. Complete the following truth table and implement the functionality using only ``AND``, ``OR``, and ``NOT``

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