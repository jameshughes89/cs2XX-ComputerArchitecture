*******************
Combinational Logic
*******************

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



Decoder
=======

#. Create a 3 bit decoder with ``AND`` gates

    * Do not use the decoder component
	* Right clicking on a gate allows for editing some properties
    * The inputs on the ``AND`` gates may be directly inverted


#. Create a 3 bit decoder with ``AND``\s and only 3 ``NOT``\s

    * Do not use the decoder component
    * The inputs on the ``AND`` gates may not be directly inverted

        * Do not change it such that their inputs have circles



Multiplexers
============

#. Create an 8 input multiplexer with logic gates

    * Do not use the multiplexer component
    * An 8 input multiplexer requires 3 selector bits


#. Create a demultiplexer with logic gates that can output to one of 4 signal lines

    * Do not use the demultiplexer component
    * Only 2 selector bits are required to select one of 4 lines


#. Connect the multiplexer and demultiplexer such that one of 8 input lines can be mapped to one of 4 output lines

    * This requires two sets of selector bits



Programmable Logic Arrays
=========================

#. Create a Programmable Logic Array (PLA) to implement the following functionality

    .. list-table::
        :widths: auto
        :header-rows: 1

        * - a
          - b
          - ci
          -
          - s
          - co
        * - ``0``
          - ``0``
          - ``0``
          -
          - ``0``
          - ``0``
        * - ``0``
          - ``0``
          - ``1``
          -
          - ``1``
          - ``0``
        * - ``0``
          - ``1``
          - ``0``
          -
          - ``1``
          - ``0``
        * - ``0``
          - ``1``
          - ``1``
          -
          - ``0``
          - ``1``
        * - ``1``
          - ``0``
          - ``0``
          -
          - ``1``
          - ``0``
        * - ``1``
          - ``0``
          - ``1``
          -
          - ``0``
          - ``1``
        * - ``1``
          - ``1``
          - ``0``
          -
          - ``0``
          - ``1``
        * - ``1``
          - ``1``
          - ``1``
          -
          - ``1``
          - ``1``


#. Create a new design using Digital's Synthesis tool

    * The tool can be found under "Analysis -> Synthesis"
    * The tool is tedious to use


#. Create the same functionality with a Look Up Table

    * Can be found under "Components -> Logic -> Lookup Table"


#. Simplify the circuit design by reducing the number of gates that are used

    * Try gate types other than ``NOT``, ``OR``, and ``AND``
