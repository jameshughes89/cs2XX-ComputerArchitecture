**************
Enhancing ESAP
**************

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



Including Hardware
==================

For this part of the lab, use the ESAP digital file
:download:`from here. <../../topics/control-logic/esap_alu_ram_output_pc_instruction_control.dig>`


#. Include the hardware for ``AND``, ``OR``, and ``NOT`` operations to the ESAP system

    * These operators will work similar to addition to subtraction in how they work
    * Apply the operator to the contents of the A and B registers, and store the result in the A register

        * ``NOT`` only works on the contents of the A register


#. These new operators require control signals

    * Connect these new control signals to the control logic loop up table



Control Logic
=============

For this part of the lab, use the script for generating the control logic patterns
:download:`from here. <../../topics/control-logic/create_control_logic_patterns_for_look_up_table.py>`


#. Although the new control logic is connected, ensure the look up table has the correct number of outputs

    * Ensure the number of outputs from the look up table includes the new control signals


#. Update the contents of the look up table to allow for three new machine code instructions

    * An instruction for each of the operators allowed by the new hardware
    * Use the 3 unused patterns for these instructions
    * Use the Python script to create a new hex file for the look up table


#. Write machine code programs to ensure each of these new instructions work properly



Enhancing the Previous Lab
==========================

#. If not already completed, finish the design from the previous lab


16 Bit Bus
----------

#. In a separate circuit, create a design for a 16 bit bus using

    * RAM with an 8 bit address space and 8 bit addressability (:math:`265 \times 8` bits)
    * A counter
    * Two 8 bit instruction registers

        * Even counter values retrieve data from even RAM addresses, and odd values retrieve from odd memory addresses
        * Fetching from RAM takes 2 clock cycles
        * One of the two 8 bit registers will always store bit patterns from the even or odd memory addresses
        * The output from these two 8 bit registers make up the 16 bit bus


#. Add this design to the larger design from the previous labs

    * Include it in the design such that bit patterns can be written to RAM and executed automatically

        * The bit patterns as discussed in previous labs


    * Not all of the 16 bits will be needed when interfacing with the previous design









