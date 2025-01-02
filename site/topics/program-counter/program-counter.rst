===============
Program Counter
===============

* As of now, only data was stored in RAM
* However, RAM will eventually be used to store instructions in addition to data

    * Although, instructions are data


* These instructions are retrieved from RAM one at a time, and the system then executes the instruction
* The program counter is a component that keeps track of the memory address of the next instruction

    * It effectively keeps track of which *line* of the program is to be run next



Program Counter Module
======================



Including the Program Counter in the System
===========================================

* To add the program counter to the ESAP system, connect the corresponding components

.. figure:: esap_alu_ram_output_pc.png
    :width: 500 px
    :align: center

    Configuration of the ESAP system with the ALU, RAM, output, and program counter modules connected.


* As with the previous modules, the control signals are moved to the bottom

    * The order of the control signals, from left to right, is not important
    * The current order was selected for visual clarity and consistency of the control bus


* Again, as with previous modules, the placement of the program counter is not important

    * It's placement was selected to match the architecture overview


.. figure:: esap_alu_ram_output_pc_vs_architecture_overview.png
    :width: 666 px
    :align: center

    Comparison of the current system and the ESAP architecture overview.



Using the Program Counter in the System
=======================================



For Next Time
=============

* Something?


