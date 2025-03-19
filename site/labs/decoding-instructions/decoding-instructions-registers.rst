*****************************************
Bit Patterns, Instructions, and Registers
*****************************************

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


Prepare
=======

#. If not already completed, finish the design from the previous lab



Registers
=========

#. Modify the design such that the values do not come from 8 bit inputs, but from registers

    * This will be similar to assignment 3
    * The updated design should include eight 8 bit registers
    * Two sets of 3 bit values will be used to specify the two registers the values should be retrieved from
    * The design will have 1 output
    * This new design will have a total of 10 inputs

        * One 1 bit input specifying ALU or comparator
        * One set of 3 bit inputs specifying an operator
        * Two sets of 3 bit inputs specifying the sources of the two inputs to the ALU/comparator


#. Modify the design such that the result is not only output, but saved to a specified register

    * This design will have 1 output
    * This design will have 13 inputs

        * The same 10 inputs discussed above
        * An additional 3 inputs specifying which register the output should be saved to

