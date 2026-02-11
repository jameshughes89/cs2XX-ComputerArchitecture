************
Assignment 3
************

* **Worth**: 5%
* **DUE**: Monday March 2, 11:55pm; submitted on MOODLE.



Provided Files
==============

Incomplete Digital files are provided for the questions. These files contain tests, a resizable designated space for
building circuits, and labelled inputs, outputs, and other components.

:download:`These files can be downloaded from here. <assignment_3-dig_files.zip>`

Uncompress this folder and open the files within Digital. Each question specifies which of the file to work in.



Part 1 --- Registers
====================

#. Create a circuit to swap data between several registers

    * Use the provided file titled "1_1-register_swap.dig"
    * Data can be moved between 8 different sources/destinations

        * Seven 8 bit registers
        * The circuit will also have the ability to read/write from data in/out

            * The source may be data in, or the destination may be data out


    * This circuit will have one 8 bit output serving as data out
    * This circuit will have a total of 8 inputs

        * A clock input
        * One 8 bit input serving as the data in
        * Three bits specifying the source

            * Registers 0 -- 6 are referred to by their corresponding bit patterns

                * For example, ``011`` refers to register 3


            * Data in is referred to by the bit pattern ``111``


        * Three bits specifying the destination

            * Registers 0 -- 6 are referred to by their corresponding bit patterns
            * Data out is referred to by the bit pattern ``111``


    * For example, consider the following source and destination bit patterns

        * ``111`` ``000`` --- move the contents from data in into register 0
        * ``000`` ``001`` --- move the contents from register 0 into register 1
        * ``001`` ``111`` --- move the contents from register 1 to data out



Part 2 --- ALU
==============

#. Create an ALU capable of performing 8 unique operations

    * Use the provided file titled "2_1-alu.dig"
    * This circuit has one eight bit output
    * This circuit has a total of 5 inputs

        * One 8 bit input specifying operand A for the ALU
        * Another 8 bit input specifying operand B
        * Three 1 bit inputs specifying an operator to apply to the operands
        * **Note:** This circuit will likely require a constant value input, which is not counted here


    * The eight operations are as follows

        * Return A unchanged --- :math:`f(A, B) = A`
        * 2s complement negation --- :math:`f(A, B) = -A`

            * Use the built in Digital component under the Arithmetic components


        * ``NOT`` A --- :math:`f(A, B) = \lnot A`
        * ``OR`` --- :math:`f(A, B) = A \lor B`
        * ``AND`` --- :math:`f(A, B) = A \land B`
        * ``XOR`` --- :math:`f(A, B) = A \oplus B`
        * Addition --- :math:`f(A, B) = A + B`
        * Subtraction --- :math:`f(A, B) = A - B`


    * The three 1 bit inputs specify the operator in the above order
    * **Note:** The first three operators ignore the B input



Part 3 --- Comparator
=====================

For these questions, do not use the built in comparator component.

#. Create a circuit that can perform a specific comparison of two inputs

    * Use the provided file titled "3_1-comparator.dig"
    * This circuit must use an 8 input/3 selector bit multiplexer
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
    * **Note:** ``000`` and ``100`` ignore the inputs


#. Create another circuit that can perform a specific comparison of two inputs

    * Use the provided file titled "3_2-comparator.dig"
    * This question is the same as above, but with a constraint
    * This circuit may not use an 8 input/3 selector bit multiplexer

        * This circuit may use one 2 input/1 selector bit multiplexer
        * **Hint:** Consider using ``AND`` gates as a way to activate/deactivate signals



Part 4 --- ALU from Registers
=============================

#. Create a circuit capable of applying ALU operators to data from specific registers, and save the result to a register

    * Use the provided file titled "4_1-alu_reg.dig"
    * This circuit combines the core ideas from Parts 1 and 2 (not part 3)
    * This circuit will have one 8 bit output serving as data out
    * This circuit will have a total of 14 inputs

        * A clock input
        * One 8 bit input serving as the data in
        * Three 1 bit inputs specifying the ALU operator to perform
        * Three 1 bit inputs specifying the source register (or data in) for operand A
        * Three 1 bit inputs specifying the source register (or data in) for operand B
        * Three 1 bit inputs specifying the destination register (or data out) to send the result of the operation


    * For example, consider the following operator, A, B, and destination bit patterns

        * ``000`` ``111`` ``000`` ``000`` --- Data in as A, store A in register 0
        * ``000`` ``111`` ``000`` ``001`` --- Data in as A, store A in register 1
        * ``110`` ``000`` ``001`` ``110`` --- Register 0 as A, register 1 as B, store A + B in register 6
        * ``000`` ``110`` ``000`` ``111`` --- Register 6 as A, put result in data out



Some Hints
==========

* Work on one part at a time
* Some parts of the assignment build on the previous, so get each part working before you go on to the next one
* Test each design as you build it

    * This is a really nice thing about these circuits; you can run your design and see what happens
    * Mentally test before you even implement --- what does this design do? What problem is it solving?


* If you need help, ask

    * Drop by office hours



Some Marking Details
====================

.. warning::

    Just because your design produces the correct output and the tests pass, that does not necessarily mean that you
    will get perfect, or even that your design is correct.


Below is a list of both *quantitative* and *qualitative* things we will look for:

* Correctness?
* Did you follow instructions?
* Label names?
* Design, layout, and style?
* Did you do weird things that make no sense?



What to Submit to Moodle
========================

* Submit your completed Digital (*.dig*) files to Moodle
* Do **not** compress the files before uploading to Moodle


.. warning::

    Verify that your submission to Moodle worked. If you submit incorrectly, you will get a 0.



Assignment FAQ
==============

* :doc:`See the general FAQ </assignments/faq>`
