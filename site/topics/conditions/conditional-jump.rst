=============================
Conditional Jump Instructions
=============================

* The various status flag values can now be determined and stored in the flags register
* However, how should the conditional jumps be handled by the control logic?
* Further, the existing control logic needs to be updated to now handle the new flag register control signal

    * When should the system's status signal values be stored stored in the flags register?



Conditional Jump Control Logic
==============================



Including the Flag Register in the System
=========================================

* Physically including the status logic and the flags register is a matter of connecting it to the existing system

* Connect the output of the ALU to the input of the condition status logic
* Replace the old control logic look up table design with the new one

    * The 3 output from the flags register are connected to the inputs to the look up table
    * The 1 new output from the look up table connects to the status flag register's enable
    * Notice the cycle --- the flags register controls the control logic, which controls the flags register


.. figure:: esap_alu_ram_output_pc_instruction_control_flag.png
    :width: 666 px
    :align: center

    Configuration of the ESAP system with the status condition logic and the flags register included. The ESAP system is
    now computationally complete.


* The contents of the look up table needs to be updated to account for the changes

    * Three new commands for the three different conditional jumps
    * Three new status signals serving as inputs to the look up table
    * An additional output signal from the look up table


* A modified version of the script used before to generate the hex file for the look up table will be used

* Like before, constants will be used to specify the position of the control signal's bit

    * Here, there are a total of 18 bits, which is one more than before
    * This corresponds to the control signal for the status flag register enable


.. literalinclude:: create_control_logic_with_flag_patterns_for_look_up_table.py
    :language: python
    :lineno-match:
    :emphasize-lines: 5
    :start-after: # [begin-control_signal_pattern_constants]
    :end-before: # [end-control_signal_pattern_constants]


* Since the conditional jump instructions are special, their operator bit patterns will be made constants

.. literalinclude:: create_control_logic_with_flag_patterns_for_look_up_table.py
    :language: python
    :lineno-match:
    :start-after: # [begin-conditional_jump_opcodes]
    :end-before: # [end-conditional_jump_opcodes]


* Similar to before, the microcode instructions will be stored in a list
* The specific microcodes for each instruction are created with bitwise OR on the control signal constants

* The difference here versus before is

    * The inclusion of the ``FLG`` signal on the addition and subtraction instructions
    * The labelling of ``JMPZ``, ``JMPS``, and ``JMPC`` instructions

        * Notice that they are still effectively ``NOOP`` instructions here
        * This will be their *standard* behaviors
        * Only under the special conditions do they act like jump instructions


.. literalinclude:: create_control_logic_with_flag_patterns_for_look_up_table.py
    :language: python
    :lineno-match:
    :emphasize-lines: 9-10, 12-14
    :start-after: # [begin-instruction_microcodes]
    :end-before: # [end-instruction_microcodes]



CASES WHERE WE NEED TO DEAL WITH CONDITIONAL JUMPS

Show saving




Programming with Conditional Jumps
==================================



For Next Time
=============

* Something?


