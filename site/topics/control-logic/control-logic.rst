=============
Control Logic
=============

* Instructions are fetched and put into the instruction register for processing

    * An instruction set has already been defined
    * Each instruction's microcodes are known

        * How the hardware is manipulated for each instruction


* However, there is still no way for the system to manipulate its own control logic

    * There is no way for the system to take an instruction and then activate/deactivate the various hardware modules


* In other words, how can the system know how to physically perform an instruction



Instruction and Microcode Steps
===============================



Look Up Table to Process Instruction
====================================



Including the Control Logic Module in the System
================================================

* Adding the control logic look up table to the system requires a reconfiguration of the control signals

    * The toggles for each control signal is removed as each signal is connected to the output of the look up table


.. figure:: esap_alu_ram_output_pc_instruction_control.png
    :width: 666 px
    :align: center

    Configuration of the ESAP system with the ALU, RAM, output, program counter, instruction register and control logic
    modules connected.


* In addition to connecting the control signals, logic was added to the system to control when the clock is active

    * This allows for the :math:`Halt` signal to halt the system
    * When :math:`Halt` is high, the clock is disabled
    * This is achieved by inverting the :math:`Halt` signal and ``AND``\ing it with the clock signal


* Further, the data input toggles were removed from the top of the bus since there is no need for them anymore

    * All data the system needs will be programmed into RAM
    * There will be no need to add data to these lines while the system is running



IMAGE OF OVERVIEW


For Next Time
=============

* Something?


