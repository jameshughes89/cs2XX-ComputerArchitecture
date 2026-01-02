************
Assignment 4
************

* **Worth**: 5%
* **DUE**: Friday TBD, 11:55pm; submitted on MOODLE.



Provided Files
==============

Incomplete Digital, hex and esap files are provided for the questions.

:download:`These files can be downloaded from here. <assignment_4-dig_files.zip>`

Uncompress this folder and open the files as necessary. Each question specifies which of the file to work in.



Part 1 --- Machine Code
=======================

.. note::

    External programs can be added to RAM within Digital through **Edit -> Circuit specific settings -> Advanced**.
    Select the **Preload program memory at startup** checkbox and navigate and the select the desired hex file for
    the **Program file** field.


#. Write a machine code program to animate ``1`` "bouncing" across the output display on repeat, as seen below

    * For this question, use the provided "1-ESAP.dig" system for running the program
    * Write the machine code program in the provided "1-bounce.hex" file

    .. figure:: bounce.gif
        :width: 250 px
        :align: center

        Demonstration of the number ``1`` "bouncing" across the output display.



#. Create a new "bouncing" program such that the delay between each step of the animation is the same

    * Due to jump, the time delay between the updates to the output register is likely inconsistent
    * Change the program such that there is an even time delay between each update
    * If the solution to the previous question already addressed this, simply repeat it here
    * For this question, use the provided "1-ESAP.dig" system for running the program
    * Write the machine code program in the provided "2-bounce_timing.hex" file


#. Write a program to calculate and output the result of ``55 + 66`` and ``55 - 50``

    * For this question, use the provided "1-ESAP.dig" system for running the program
    * Write the machine code program in the provided "3-arithmetic.hex" file



Part 2 --- New Instructions
===========================

Because outputting a value requires saving it to RAM before it can be displayed (``SAVA`` + ``OUTU``, for example), it
effectively takes up 2 RAM addresses. This may become problematic as the system only has 16 bytes of RAM.

#. Create two new instructions to output an unsigned or signed integer directly from the A register

    * Have ``0b1011`` and ``0b1100`` be the instructions for an unsigned and signed integer respectively
    * These instructions take no operand
    * Modify the contents of the look up table in the provided "4-ESAP.dig" file to add the new instructions

        * **Hint:** Use a script to generate the hex values for the control logic look up table


#. Using the new instructions, calculate and output the result of ``55 + 66``,  ``55 - 50``, and ``66 - 55``

    * This must be done in a single program
    * Use the modified "4-ESAP.dig" file from the previous question for running the program
    * Write the machine code program in the provided "5-arithmetic_big.hex" file



Part 3 --- Eliminating Clock Cycles
===================================

Currently, each instruction within the system always takes 4 microcode steps (clock cycles), even if the instruction
only really needs 3. For example, consider that the ``LDAD`` instruction only needs the 2 fetch steps + 1 more step to
output from the instruction register and input into the A register.

#. Modify the ESAP design and instruction set such that instructions complete in 3 clock cycles, where possible

    * For this question, do not include the new output instructions from the previous part
    * This question requires modifying the hardware of the ESAP system and the control logic look up table
    * Use and modify the provided "6-ESAP.dig" file

        * Use a script to generate the hex values for the control logic look up table


    * Although there is an argument for leaving ``NOOP`` 4 clock cycles, make it take 3 here



Part 4 --- Assembly
===================

Writing simple programs in machine code is arguably not too difficult, but remembering machine code is a tedious task.
When solving more complex problems, eliminating unnecessary difficulty helps improve the programming experience.

#. Write a program in the ESAP assembly language that can divide 2 numbers and output the result

    * To simplify things, assume

        * The numbers are evenly divisible (no remainder)
        * Only positive integers
        * The answer will always be at least ``1`` (one would not ask ``0/5``, for example)


    * Have the dividend and divisor be in addresses 14 and 15 respectively
    * For this question, use the provided "7-ESAP_conditions.dig" system for running the program

        * This solution will not make use of the modified ESAP systems from the previous questions
        * No new instructions or 3 microcode step instructions


    * Write the assembly code program in the provided "7-divide.esap" file
    * Use the provided "assembler.py" to assemble to machine code



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

* Submit your modified ESAP Digital (*.dig*) files to Moodle
* Submit your completed hex files for the machine code programs
* Submit your completed esap file for the divide assembly program
* Submit the hex files for modifying the look up tables
* Do **not** compress the files before uploading to Moodle


.. warning::

    Verify that your submission to Moodle worked. If you submit incorrectly, you will get a 0.



Assignment FAQ
==============

* :doc:`See the general FAQ </assignments/faq>`
