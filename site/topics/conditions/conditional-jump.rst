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



new script for this
SHOW CODE EXAMPLES



Programming with Conditional Jumps
==================================



For Next Time
=============

* Something?


