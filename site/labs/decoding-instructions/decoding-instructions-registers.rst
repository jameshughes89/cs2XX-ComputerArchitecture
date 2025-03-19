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



New Operation
=============

Currently there is no way to actually load data into the system.

#. Add a new mode/instruction such that data can be loaded into a specific register

    * Currently 1 bit is used to specify ALU or comparator operations, or *modes*
    * Add an additional bit to allow for selecting between up to 4 modes

        * 2 mode bits
        * 3 bits that served as selecting a specific operation
        * Two sets of 3 bits for specifying 2 source registers
        * 3 bits for a destination register


    * Update the system such that one of these 4 modes allows for loading data directly to a register

        * The 3 destination register bits specify where the data is to be stored
        * 8 bits of the 9 available for the operator and 3 source registers specify the 8 bit data


    * For example, consider the below bit patterns and their meanings

        * ``00 110 101 010 111`` --- ``add`` on registers 5 and 2 and store in 7
        * ``01 110 101 010 111`` --- ``>=`` on registers 5 and 2 and store in 7
        * ``10 1 10101010 111`` --- Store ``0b10101010`` (``170``) in register 7



#. Add a new mode such that data can be moved between registers

    * Here, only one set of 3 bits specifying the source register is required
    * ``11 110 101 010 111`` --- Move contests of register 2 to register 7