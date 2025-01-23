************
Assignment 1
************

* **Worth**: 5%
* **DUE**: January 27, 11:55pm; submitted on MOODLE.



Provided Files
==============

Incomplete Digital files are provided for the questions for Part 2. These files contain tests, designated space for
building circuits, and labelled inputs and outputs.

:download:`These files can be downloaded from here. <assignment_1-dig_files.zip>`

Uncompress this folder and open the files within Digital. Each question specifies which of the file to work in.



Part 1 --- Non-Digital
======================

This portion of the assignment will not make use of the Digital simulation software. All answers must be typed and use
proper math typesetting, where appropriate.

#. Given the 26 letters of the alphabet

    a. What is the fewest number of bits needed to give each letter a unique bit pattern?
    b. How many bits would be needed for both lowercase and uppercase letters?
    c. How many bits would be needed to identify uppercase and lowercase letters, and numerals (the 10 digits)?


#. Create a table showing all 4 bit binary integers and their corresponding decimal value.

    .. list-table:: Example start of the table
        :widths: 50 50
        :header-rows: 1

        * - Binary
          - Decimal
        * - :math:`0000_{2}`
          - :math:`0_{10}`
        * - :math:`0001_{2}`
          - :math:`1_{10}`
        * - ``...``
          - :math:`...`
        * - ``...``
          - :math:`...`


#. Convert the following binary (base 2) numbers to decimal (base 10) --- show all work.

    a. :math:`10101010_{2}`
    b. :math:`01010101_{2}`
    c. :math:`11111010_{2}`


#. Convert the following decimal (base 10) numbers to binary (base 2) --- show all work.

    a. :math:`123_{10}`
    b. :math:`31_{10}`
    c. :math:`128_{10}`


#. Convert the following numbers between the specified bases --- show all work.

    a. :math:`123_{5}` = :math:`?_{4}`
    b. :math:`123_{7}` = :math:`?_{8}`
    c. :math:`123_{8}` = :math:`?_{16}`


#. Add the following binary numbers and leave the result in binary --- show all work (e.g. carrying).

    * For visual clarity, the typesetting of binary numbers is changed for this and the following questions.

    a. ``1010 + 101``
    b. ``1010011 + 101011``
    c. ``1111 + 1``


#. Perform the following bitwise boolean operations (perform the operation on each bit, in order, to obtain the result).

    a. ``NOT 1010``
    b. ``1010 AND 1100``
    c. ``1010 OR 1100``


#. Generate truth tables for each of the following binary expressions.

    a. :math:`\lnot a \land b`
    b. :math:`a \lor (a \land b)`
    c. :math:`\lnot a \land \lnot b`


#. Demonstrate the two De Morgan's laws with truth tables (one table for each).


#. With truth tables, show how :math:`and`, :math:`or`, and :math:`not` operations can be achieved with only

    a. :math:`nand`
    b. :math:`nor`



Part 2 --- Digital
==================

This portion of the assignment will make use of the Digital simulation software.

#. Create :math:`not`, :math:`or`, and :math:`and` gates with N-channel transistors.

    * Use the provided file titled "1-not_or_and.dig"
    * Use the corresponding space within the provided file
    * You may move the inputs and outputs if necessary and resize the labelled boxes
    * Run tests to ensure functional correctness


#. Create :math:`nor` and :math:`nand` with three N-channel transistors each.

    * Use the provided file titled "2-nor_nand_three.dig"
    * Use the corresponding space within the provided file
    * You may move the inputs and outputs if necessary and resize the labelled boxes
    * Run tests to ensure functional correctness


#. Create :math:`nor` and :math:`nand` with two N-channel transistors each.

    * Use the provided file titled "3-nor_nand_two.dig"
    * Use the corresponding space within the provided file
    * You may move the inputs and outputs if necessary and resize the labelled boxes
    * Run tests to ensure functional correctness
    * **Hint** Take special note of the design of the :math:`not` gate built with a transistor


#. Create :math:`not`, :math:`or`, and :math:`and` using only :math:`nand` transistor configurations

    * Use the provided file titled "4-nand_universal.dig"
    * Use the corresponding space within the provided file
    * You may move the inputs and outputs if necessary and resize the labelled boxes
    * Run tests to ensure functional correctness


#. Create :math:`not`, :math:`or`, and :math:`and` using only :math:`nor` transistor configurations

    * Use the provided file titled "5-nor_universal.dig"
    * Use the corresponding space within the provided file
    * You may move the inputs and outputs if necessary and resize the labelled boxes
    * Run tests to ensure functional correctness


#. Create :math:`xor` (exclusive or) with N-channel transistors

    * Use the provided file titled "6-xor.dig"
    * Use the corresponding space within the provided file
    * You may move the inputs and outputs if necessary and resize the labelled boxes
    * Run tests to ensure functional correctness



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

* Submit any necessary PDF files to Moodle

    * Submissions for the non-digital portion of assignments that are not PDFs will not be marked
    * PDFs must be generated from typed documents

        * No PDFs of written work


    * If necessary, save or print word processor files as PDFs


* Submit your completed Digital (*.dig*) files to Moodle
* Do **not** compress the files before uploading to Moodle


.. warning::

    Verify that your submission to Moodle worked. If you submit incorrectly, you will get a 0.



Assignment FAQ
==============

* :doc:`See the general FAQ </assignments/faq>`
