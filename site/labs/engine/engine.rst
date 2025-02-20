*************
Little Engine
*************

* Feel free to use your laptop
* You are strongly encourage to work with others

    * When you get stuck, ask those sitting around you for help
    * Get used to working together in the labs
    * Peer teaching and peer learning has been empirically shown to be very effective


For these questions, feel free to use a single Digital workspace for all the circuits. However, label each circuit with
labelled rectangles. These are components that can be found under **Components -> Misc. -> Decoration -> Rectangle**.

Where possible, each question should have complete tests. The test component can be found under
**Components -> Misc. -> Test case**. Once a test component is placed on the workspace, right click on the component to
edit the test data.

Questions may have restrictions on the logic gates that may be used. When restrictions are stated, they only apply to
the gates; inputs, outputs, wires, etc. may be still be used.



Full Adders
===========

#. Create a circuit to add two 8 bit numbers together and output the resulting 8 bit number

    * Ignore overflows beyond 8 bits
    * Use 8 input components and 8 output components to represent the inputs/outputs
    * You may use an adder component



Doubling and Halving
====================

#. Using a adder, create a circuit to double some 8 bit number

    * Ignore overflows beyond 8 bits


#. Without using an adder, create a circuit to double some 8 bit number

    * **Hint:** This can be done with very few components
    * Ignore overflows beyond 8 bits


#. Create a circuit to half some 8 bit number

    * Ignore *underflows*



Counting Signals
================

#. Create a circuit to determine if the number of high input signals is even or odd

    * This circuit must have 4 inputs and 1 output
    * Output ``0`` when an even number of the 4 input bits are high
    * Output ``1`` when an odd number of the input bits are high


#. Create a circuit to determine if 2 or more input signals are high

    * This circuit must have 4 inputs and 1 output
    * Output ``0`` when fewer than 2 input signals are high
    * Output ``1`` when 2 or more input signals are high


#. Create a circuit that determines the number of high input signals

    * This circuit must have 4 inputs and 3 outputs
    * The output will be the number of high input signals in binary
    * Below are examples of ``inputs`` -> ``outputs``

        * ``0000`` -> ``000``
        * ``0100`` -> ``001``
        * ``1001`` -> ``010``
        * ``1101`` -> ``011``
        * ``1111`` -> ``100``



Logic Engine
============

#. Create a circuit that can perform ``OR``, ``NAND``, ``NOR``, and ``AND`` on two 8 bit binary patterns

    * This circuit will have a total of 18 inputs

        * This circuit will have two sets of 8 bit inputs for the binary patterns (16 inputs)
        * This circuit will also have two more input signals for specifying which operation to perform

            * ``00`` --- ``OR``
            * ``01`` --- ``NAND``
            * ``10`` --- ``NOR``
            * ``11`` --- ``AND``


    * The output will be a single 8 bit pattern representing the result


#. Create the same functionality as above, but only use

    * 1 ``OR`` gate
    * 3 ``NOT`` gates
    * 3 multiplexers
