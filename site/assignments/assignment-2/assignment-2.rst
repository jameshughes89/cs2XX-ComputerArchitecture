************
Assignment 2
************

* **Worth**: 5%
* **DUE**: Monday March 3, 11:55pm; submitted on MOODLE.



Provided Files
==============

Incomplete Digital files are provided for the questions. These files contain tests, a resizable designated space for
building circuits, and labelled inputs, outputs, and other components.

:download:`These files can be downloaded from here. <assignment_2-dig_files.zip>`

Uncompress this folder and open the files within Digital. Each question specifies which of the file to work in.



Part 1 --- Selectors
====================

#. Create a circuit where the output of some input can be inverted with some other signal

    * Use the provided file titled "1-bit_inverter.dig"
    * Below is a truth table describing the desired functionality

    .. list-table:: Bit Inverter Truth Table
        :widths: auto
        :align: center
        :header-rows: 1

        * - Input
          -
          - Invert
          -
          - Output
        * - ``0``
          -
          - ``0``
          -
          - ``0``
        * - ``0``
          -
          - ``1``
          -
          - ``1``
        * - ``1``
          -
          - ``0``
          -
          - ``1``
        * - ``1``
          -
          - ``1``
          -
          - ``1``



#. Create a 1 bit selector circuit such that one of two inputs is mapped to the output with the following constraints

    * A multiplexer may not be used
    * Only drivers and not gates may be used
    * Use the provided file titled "2-input_selector.dig"
    * Below is a truth table describing the desired functionality

        * Here, ``A`` and ``B`` are variable inputs that can take on either ``0``/``1``


    .. list-table:: 1 Bit Selector Truth Table
        :widths: auto
        :align: center
        :header-rows: 1

        * - :math:`i_{0}`
          - :math:`i_{1}`
          -
          - :math:`s`
          -
          - :math:`o`
        * - ``A``
          - ``B``
          -
          - ``0``
          -
          - ``A``
        * - ``A``
          - ``B``
          -
          - ``1``
          -
          - ``B``



#. Create a circuit that can map one of two inputs to one of two outputs with the following constraints

    * A multiplexer may not be used
    * Only drivers and not gates may be used
    * **Hint:** Use the general bit selector design from the previous question
    * Use the provided file titled "3-input_output_selector.dig"
    * Below is a truth table describing the desired functionality

        * Note that ``Z`` denotes the high impedance state and does not represent some variable input

    .. list-table:: 1 Bit Input/Output Selector Truth Table
        :widths: auto
        :align: center
        :header-rows: 1

        * - :math:`i_{0}`
          - :math:`i_{1}`
          -
          - :math:`s_{i}`
          - :math:`s_{o}`
          -
          - :math:`o_{0}`
          - :math:`o_{1}`
        * - ``A``
          - ``B``
          -
          - ``0``
          - ``0``
          -
          - ``A``
          - ``Z``
        * - ``A``
          - ``B``
          -
          - ``0``
          - ``1``
          -
          - ``Z``
          - ``A``
        * - ``A``
          - ``B``
          -
          - ``1``
          - ``0``
          -
          - ``B``
          - ``Z``
        * - ``A``
          - ``B``
          -
          - ``1``
          - ``1``
          -
          - ``Z``
          - ``B``


#. Create a circuit that can map one of four inputs to one of four outputs with the following constraints

    * Multiplexers and demultiplexer may be used
    * Use the provided file titled "4-plex_input_output_selector.dig"



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

    * Use the provided file titled "5-JK_flipflop.dig"
    * Feel free to research designs of a JK flop-flop

        * **WARNING:** Most designs available will fail due to race conditions


    * **HINT:** Use the idea of the D flip-flop design for the JK flop-flop to resolve the race condition problem

        * **WARNING:** Unlike the the D flip-flop, have the final :math:`Q` value latch when the clock goes low



#. Create a 4 bit counting circuit that increments 1 every clock pulse with 4 JK flip-flops

    * For example, each arrow corresponds to one clock pulse

        * ``0000`` -> ``0001`` -> ``0010`` -> ``0011`` -> ``0100`` -> ``0101`` -> ... -> ``1111`` -> ``0000`` -> ...


    * Use the provided file titled "6-counter.dig"
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

    * Use the provided file titled "7-4_byte_ram.dig"
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
