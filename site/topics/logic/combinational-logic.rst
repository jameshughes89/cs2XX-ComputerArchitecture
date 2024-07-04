*******************
Combinational Logic
*******************

* With an understanding of logic gates, more complex logic structures can be constructed
* Here, structures that can make decisions based on some combination of inputs will be explored



Decoders
========

* Consider a situation where an input signal controls two outputs, where only one should be active at a time

    * When the input signal is low, one of the two outputs is high
    * When the input signal is high, the other output should be high


.. list-table:: Single Bit Decoder
    :widths: auto
    :align: center
    :header-rows: 1

    * - Input
      -
      - Output a
      - Output b
    * - ``0``
      -
      - ``1``
      - ``0``
    * - ``1``
      -
      - ``0``
      - ``1``


.. note::

    Until now, all truth tables were shown to demonstrate how the boolean operators worked, each taking some number of
    inputs and producing a single output. These truth tables were used to describe how each operator worked.

    Here, the truth table is not describing any specific operator, but some desired functionality. The goal would then
    be to construct some circuit with logic gates to produce the desired functionality.  Further, it's showing how the
    desired functionality has more than one output. More specifically, when the input is ``0``, output a should be ``0``
    and output b should be ``1``, and when the input is ``1``, output a should be ``1`` and output b should be ``0``.


* Based on the truth table, how could this functionality be achieved with boolean operators?

    * Output a is the inversion of the input
    * Output b is simply the input


.. figure:: single_bit_decoder.png
    :width: 500 px
    :align: center

    A single bit decoder. At any point in time, a single output is always high. The specific output that is high is
    controlled by the input signal.


* This is an example of a single bit decoder

    * The one input signal can be thought of as a single bit
    * The input signal is "decoded" to control the output signals


More than One Input Bit
-----------------------

* Now consider a situation where four separate circuits need to be controlled by a decoder

    * These circuits will be labeled 0 to 3 for ease


* There needs to be a way to specify which of the four circuits should be running at any given time
* Unfortunately, a single bit of information can only be decoded to two states --- ``0``/``1``
* However, two input signals can have a total of four unique states

* Continuing the idea that a signal can be thought of as a single bit, two signals can represent a two bit binary number
* Each of these binary numbers could then correspond to each of the 0 -- 3 circuits

.. figure:: signals_as_bits.png
    :width: 500 px
    :align: center

    All four states two signals can represent. If treating the signals as bits, these correspond to the numbers, from
    left to right, :math:`00_{2}`, :math:`01_{2}`, :math:`10_{2}`, and :math:`11_{2}`, which correspond to the numbers
    :math:`0_{10}`, :math:`1_{10}`, :math:`2_{10}`, and :math:`3_{10}` respectively.


* The below truth table describes the desired functionality
* Notice the relationship between the binary number the input signals represent and which output signal is high

.. list-table:: Two Bit Decoder
    :widths: auto
    :align: center
    :header-rows: 1

    * - Input a
      - Input b
      -
      - Output 0
      - Output 1
      - Output 2
      - Output 3
    * - ``0``
      - ``0``
      -
      - ``1``
      - ``0``
      - ``0``
      - ``0``
    * - ``0``
      - ``1``
      -
      - ``0``
      - ``1``
      - ``0``
      - ``0``
    * - ``1``
      - ``0``
      -
      - ``0``
      - ``0``
      - ``1``
      - ``0``
    * - ``1``
      - ``1``
      -
      - ``0``
      - ``0``
      - ``0``
      - ``1``


* To design a circuit for such functionality, think about each row and corresponding output at a time
* Consider the first row and output 0

    * When input a is *not* high *and* input b is *not* high, output high for only output 0


* This functionality can be achieved with a single two input and gate with both inputs inverted

    * This gate will only output ``1`` when both inputs are ``0``
    * Output 0 is :math:`\lnot a \land \lnot b`


.. figure:: and_gate_for_00.png
    :width: 250 px
    :align: center

    And gate with two inverted inputs. This gate will only output ``1`` when both inputs are ``0``.


* Now consider the second row and input 1

    * When input a is *not* high *and* input b is high, output high for only output 1
    * Output 1 is :math:`\lnot a \land b`


.. figure:: and_gate_for_01.png
    :width: 250 px
    :align: center

    And gate that will only output ``1`` when the input signal is ``01``, where the top signal is the most significant
    bit.



* Following this pattern, a two bit decoder can be a series of four and gates with every combination of inverted inputs

.. figure:: two_bit_decoder.png
    :width: 500 px
    :align: center

    A two bit decoder, often called a 2-4 decoder. Two input signals are decoded to control a the four output signals.
    At any time, only one of the four output signals is high.


* This particular design scales such that one can create decoders of any size

    * The only constraint, for lack of a better term, is the relationship between the number of inputs and outputs
    * Given :math:`n` inputs, a total of :math:`2^{n}` outputs can be controlled


* In general, and gates with various inverted inputs are ideal for situations where a specific input pattern is required

.. figure:: and_gate_for_01010010.png
    :width: 250 px
    :align: center

    Example of an and gate that only outputs ``1`` when an input pattern of ``01010010``, where the top input is the
    most significant bit, is observed.



Decoder Symbol
--------------

* Decoders are a common tool used in digital circuits, and as such, they are often represented with a single symbol
* There is no universally set symbol for decoders, so the symbol used for decoders could differ
* For this course, the symbol from Digital for decoders will be used

.. figure:: decoder_symbol.png
    :width: 333 px
    :align: center

    The trapezoid component represents a 2-4 decoder.


* The above image shows a 2-4 decoder

    * Two inputs
    * Four outputs


* Within this image, the input/output symbols are minimized for easier representation
* Further, the two input signals are merged into a single signal line with a splitter/merger

    * One can think of the single line entering the decoder as two separate signals


* The splitter/merger is used to simplify circuit designs to condense the number of signal lines

.. figure:: merge-4-split-4.png
    :width: 333 px
    :align: center

    Example of four signals being merged into a single line and then being split into the four signal lines. This has no
    purpose other than to demonstrate how the splitter/merger works.



Multiplexers
============



Programmable Logic Arrays
=========================



Functional Completeness
=======================



For Next Time
=============

* Check out the :download:`Decoder <1-2_and_2-4_decoders.dig>` schematic for Digital
* Read Chapter 3 Sections 5 of your text

    * 3 pages