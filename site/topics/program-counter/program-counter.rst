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

* The program counter has several important functions

    * Keeps track of the memory address of the next instruction to run
    * Increment the memory address stored

        * However, this should not happen on every clock cycle
        * Instructions often take several clock cycles to complete
        * Thus, there needs to be a way to control when the program counter increments


    * Output its current value
    * Set its current value to a specific memory address

        * Important for looping and conditionals


Storing and Incrementing Values
-------------------------------

.. figure:: program_counter_count.png
    :width: 500 px
    :align: center

    Configuration of a register and adder set to add 1 to the value in the register. Although the adder is always adding
    one to the value stored in the register, the value in the register only updates when the :math:`PC_{e}` signal is
    high.


* Storing a value can be achieved with a register
* Incrementing a value can be achieved with an adder set to only ever add 1 to some inputted value

* With the above configuration, the adder is always adding 1 to the value stored/output by the register (:math:`Q`)

    * The adder's carry in is set to ``0`` and the carry out is ignored


* However, even though the value at the register's :math:`D` input is always :math:`Q+1`, it only updates when enabled

    * When the :math:`PC_{e}` control signal is set high


* This design provides control over when the counter increments


Controlling Output
------------------

.. figure:: program_counter_count_out.png
    :width: 500 px
    :align: center

    A driver can be used to control when the counter's value is output. Note that the counter's output is the register's
    output (:math:`Q`), not the output of the adder (:math:`S`).


* To control the output, use a driver like in previous designs
* Note, the counter's output is :math:`Q` --- the register's output

    * The output of the adder is for updating the state of the counter


Controlling Inputs
------------------

.. figure:: program_counter_count_out_in.png
    :width: 666 px
    :align: center

    A multiplexer and a new signal :math:`PC_i` to control which value to store to the register --- the output of the
    adder or the input data.


* In addition to incrementing, the program counter must be able to store specified input data when needed
* Therefore, the counter's register must be able to store one of two potential values

    * The output from the adder, containing the incremented value
    * Some input data from elsewhere


* A multiplexer can be used to control which of the two signals is active on the register's input :math:`D`
* A control signal :math:`PC_{i}` controls the multiplexer

    * In the above configuration, when :math:`PC_{i}` is low, the register's :math:`D` input is the incremented value
    * When :math:`PC_{i}` is high, the register's :math:`D` input is the input data


* If either :math:`PC{i}` or :math:`PC_{e}` are high, the program counter's register must be enabled


Program Counter Design
----------------------

.. figure:: program_counter.png
    :width: 500 px
    :align: center

    Program counter module with an 8 bit data bus. For the ESAP system, the program counter only needs 4 bits as there
    are 16 RAM addresses, therefore splitters/mergers are used to have the program counter interface with the bus.


* Due to ESAP's design, only 4 bits are used to index RAM

    * The least significant 4 bits on the bus


* Since the program counter is keeping track of memory addresses, the program counter only needs to manage 4 bits
* Therefore, some mechanism to interface between the two bit lengths is needed
* Here, splitters/mergers are used to fit the 4 bit program counter into the 8 bit design

    * Data from the bus is split

        * Only the least significant 4 bits are connected to the program counter's register


    * Data to the bus is merged with zeros

        * To pad the counter's 4 bit output to be a full 8 bits


Counter Component
-----------------

* Since counters are a common tool, they are often represented as a single component

.. figure:: counter_preset_symbol.png
    :width: 200 px
    :align: center

    Counter component with an input for loading in data.


* The above image shows the counter component with presets

    * A counter with the ability to load data into the counter


* This component includes several inputs not required for the ESAP's program counter

    * The clear input, which resets the counter to 0, is not needed
    * The direction input, which controls the counter direction, does not need to be manipulated

        * Only needs to count up for the ESAP system


    * For both, these inputs could be tied to constants


.. figure:: program_counter_component.png
    :width: 500 px
    :align: center

    Program counter module configuration using the built in counter component.



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

* Like before, the numbers 15 and 4 will be added together, but this time

    * All data will be stored in RAM

        * Data will not be entered into the system via the data input toggles


    * The program counter will be used to track of the memory address of the data needing to be retrieved


* Although the data input toggles will not be used, the control logic toggles will still need to be controlled

* A hex file containing the data for the numbers 15 and 4 will be created

    .. code:: text

        v2.0 raw
        0x0F
        0x04


* This file can then be loaded into RAM

.. note::

    Loading data into RAM before runtime in Digital works a little different compared to the look up tables.

    First, the RAM component needs to be marked as "Program Memory".

        .. figure:: ram_program_memory.png
            :width: 333 px
            :align: center

            "Program Memory" option selection under the Advanced tab for a RAM component.


    Then, under Digital's main menu **Edit -> Circuit specific settings** window, within the Advanced tab, select the
    "Preload program memory at startup" option and specify the "Program file" to be loaded.

        .. figure:: circuit_specific_settings_preload_program_file.png
            :width: 333 px
            :align: center

            "Preload program memory at startup" option under the Advanced tab of the circuit specific settings. Notice
            the "Program file" is specified.



* With the data in RAM, think about the steps required to perform the addition

    * Get the address of the data to be retrieved from the program counter to the address register
    * Increment the program counter

        * Remember, the idea of the program counter is that is stores the address of the *next* thing to be dealt with


    * Output the data from the specified address in RAM to register A
    * Get the address of the next data to be retrieved from the program counter to the address register
    * Increment the program counter
    * Output the data from the specified address in RAM to register B
    * Perform addition
    * Put the result of addition into the output register









program table

now subtract for fun
need to re-load A value from RAM
cam "jump" back to the start of RAM

TABLE



For Next Time
=============

* Something?


