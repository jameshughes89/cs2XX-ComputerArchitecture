************
Assignment 2
************

* **Worth**: 5%
* **DUE**: Monday February 9, 11:55pm; submitted on MOODLE.



Provided Files
==============

Incomplete Digital files are provided for the questions. These files contain tests, a resizable designated space for
building circuits, and labelled inputs, outputs, and other components.

:download:`These files can be downloaded from here. <assignment_2-dig_files.zip>`

Uncompress this folder and open the files within Digital. Each question specifies which of the file to work in.



Part 1 --- Counting With Adders
===============================

#. Create a 4 bit counting circuit that increments 1 every clock pulse using a 4 bit adder and a 4 bit register

    * Use the provided file titled "1_1-counter.dig"
    * This file already contains the components needed in the workspace

        * The design must use these components
        * No other components may be added to the design


#. Modify the counting circuit such one can control if data is being inputted to/outputted from the counter

    * Use the provided file titled "1_2-counter_load.dig"
    * An arbitrary 4 bit number may be loaded into the counter
    * Out from the counter may be controlled
    * **HINT:** In & EN would typically not be high at the same time, but both enable the register
    * This file already contains the components needed in the workspace

        * The design must use these components
        * No other components may be added to the design



Part 2 --- JK Flip-Flops
========================

An SR flip-flop is similar to an SR latch except that the flip-flop only changes state on a clock pulse, similar to that
of a D flip-flop.

A JK Flip Flop is similar to an SR flip-flop, except that when both inputs (called :math:`J` and :math:`K`, for
:math:`S` and :math:`R` respectively) are ``1``, the outputs :math:`Q` and :math:`\lnot Q` toggle/oscillate.

    .. list-table:: JK Flip-Flop Truth Table
        :widths: auto
        :align: center
        :header-rows: 1

        * - :math:`C`
          -
          - :math:`J`
          - :math:`K`
          -
          - :math:`Q`
          - :math:`\lnot Q`
          -
          - :math:`Q`
          - :math:`\lnot Q`
        * - ``C``
          -
          - ``0``
          - ``0``
          -
          - ``0``
          - ``1``
          -
          - ``0``
          - ``1``
        * - ``C``
          -
          - ``0``
          - ``0``
          -
          - ``1``
          - ``0``
          -
          - ``1``
          - ``0``
        * - ``C``
          -
          - ``0``
          - ``1``
          -
          - ``0``
          - ``1``
          -
          - ``0``
          - ``1``
        * - ``C``
          -
          - ``0``
          - ``1``
          -
          - ``1``
          - ``0``
          -
          - ``0``
          - ``1``
        * - ``C``
          -
          - ``1``
          - ``0``
          -
          - ``0``
          - ``1``
          -
          - ``1``
          - ``0``
        * - ``C``
          -
          - ``1``
          - ``0``
          -
          - ``1``
          - ``0``
          -
          - ``1``
          - ``0``
        * - ``C``
          -
          - ``1``
          - ``1``
          -
          - ``0``
          - ``1``
          -
          - ``1``
          - ``0``
        * - ``C``
          -
          - ``1``
          - ``1``
          -
          - ``1``
          - ``0``
          -
          - ``0``
          - ``1``


This toggle feature has an interesting property that the :math:`Q` output toggles at half the frequency of the clock
input. In other words, it takes two clock cycles for :math:`Q` to cycle once.



#. Create a JK flip-flop

    * Use the provided file titled "2_1-JK_flipflop.dig"
    * Feel free to research designs of a JK flop-flop

        * **WARNING:** Most designs available will fail due to race conditions


    * **HINT:** Use the idea of the D flip-flop design for the JK flop-flop to resolve the race condition problem

        * **WARNING:** Unlike the the D flip-flop, have the final :math:`Q` value latch when the clock goes low



#. Create a 4 bit counting circuit that increments 1 every clock pulse with 4 JK flip-flops

    * For example, each arrow corresponds to one clock pulse

        * ``0000`` -> ``0001`` -> ``0010`` -> ``0011`` -> ``0100`` -> ``0101`` -> ... -> ``1111`` -> ``0000`` -> ...


    * Use the provided file titled "2_2-counter.dig"
    * This circuit will not require a register
    * Use the JK flip-flop design from the above question and not the built in component

        * Using Digital's built in JK flip-flop will not produce the desired result


    * **HINT:** Chain JK flip-flops together
    * **HINT:** Set each JK flip-flop's :math:`J` and :math:`K` inputs to ``1`` with a constant

        * This puts the JK flip-flops into their toggle/oscillate state


    * Ignore the :math:`\lnot Q`\s for this circuit
    * Note that one should expect the outputs to start on some arbitrary value when running the circuit

        * Do not expect the outputs to start at ``0000``



Part 3 --- RAM
==============

#. Create a 4 byte RAM design with four 8 bit register components, a multiplexer, demultiplexer, and a driver

    * Use the provided file titled "3_1-4_byte_ram.dig"
    * This file already contains the components needed in the workspace

        * The design must use these components
        * No other components may be added to the design



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
