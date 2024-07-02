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

    Until now, all truth tables shown included boolean operators and the tables were completed to describe how the
    operators act.

    The above truth table does not include any specific boolean operators. Here, the truth table is describing the
    desired functionally without specifying any operators.


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
    * The output signal is controlled/decoded by the input pattern 


* Multi
* Generalize easy



Multiplexers
============



Programmable Logic Arrays
=========================



Functional Completeness
=======================



For Next Time
=============

* Read Chapter 3 Sections 4 & 5 of your text

    * 4 pages