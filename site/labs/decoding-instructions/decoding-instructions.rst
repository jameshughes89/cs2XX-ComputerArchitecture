*************************************
Decoding Bit Patterns as Instructions
*************************************

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


ALU
===

#. Create an ALU capable of performing 8 unique operations

    * This is the same idea as assignment 3
    * This circuit has one eight bit output
    * This circuit has a total of 5 inputs

        * One 8 bit input specifying operand A for the ALU
        * Another 8 bit input specifying operand B
        * Three 1 bit inputs specifying an operator to apply to the operands


    * The eight operations are as follows

        * Return A unchanged
        * 2s compliment negation
        * ``NOT`` A
        * ``Or``
        * ``AND``
        * ``XOR``
        * Addition
        * Subtraction


    * The three 1 bit inputs specify the operator in the above order


Comparator
==========

#. Create a circuit capable of performing 8 unique comparison operations

    * This question is *similar* to one on assignment 3
    * Here, use Digital's built in comparator component
    * This circuit has one 1 bit output

        * Output should be ``1`` when the comparison condition is true, ``0`` when false


    * This circuit has a total of 5 inputs

        * One 8 bit input specifying A
        * Another 8 bit input specifying B
        * Three 1 bit inputs specifying a comparison operator


    * The eight comparison operations are as follows

        * ``000`` --- Always output ``0``
        * ``001`` --- ``a == b``
        * ``010`` --- ``a < b``
        * ``011`` --- ``a <= b``
        * ``100`` --- Always output ``1``
        * ``101`` --- ``a != b``
        * ``110`` --- ``a >= b``
        * ``111`` --- ``a > b``


    * The three 1 bit inputs specify the operator in the above order



Decoding an Instruction
=======================

#. Create a circuit capable of performing some ALU operation or some comparison operation

    * This circuit will combine the two above designs
    * This circuit will take 20 input signals

        * One 1 bit signal specifying if the operation to be performed is from the ALU or the comparator

            * ``0`` specifies the operation is from the ALU, ``1`` for the comparator


        * Three 1 bit signals specifying the specific operation to perform from the corresponding component

            * The operator depends on if the ALU or the comparator is used


        * One set of eight 1 bit inputs specifying some data A
        * Another set of 8 1 bit inputs specifying B


    * This circuit will have eight 1 bit output signal

        * The full 8 bits will be used when performing some ALU operation
        * Only the least significant bit will be used when performing some comparator operation


    * For example

        * ``0 010 01010101 00000000`` --- Perform ``NOT`` on ``01010101``
        * ``1 010 01010101 00000000`` --- Check if ``01010101 < 00000000``

