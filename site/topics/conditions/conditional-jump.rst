=============================
Conditional Jump Instructions
=============================

* The various status flag values can now be determined and stored in the flags register
* However, how should the conditional jumps be handled by the control logic?
* Further, the existing control logic needs to be updated to now handle the new flag register control signal

    * When should the system's status signal values be stored stored in the flags register?



Conditional Jump Control Logic
==============================



Enabling Flag Register
======================

* As discussed, the status flag register needs to be enabled at specific times to work

    * Only enable when performing addition or subtraction
    * Be disabled at all other times


* However, both addition and subtraction take several clock cycles

    * Every instruction is allocated 4 clock cycles
    * But addition (``ADAB``) and subtraction (``SUAB``) only require 3

        * Fetch (2 clock cycles)
        * Output from ALU to the A register, and set the subtract signal where necessary (1 clock cycle)


* Therefore, when *exactly* should the flag enable signal be set high?





but, there are still several steps of the operation
addition and subtraction have 3 steps each
    show them


Now, the 3rd step will also include flags enable



One may reasonably  be worried about what happens the value in A gets updated at the end of the instruction
    this causes the values in the ALU to change, chaning the status flags

But this should not matter as the value in the status flag gets latched into the respective reg at the same time as A

    The value the ALU is calculating changes, but not before the value of the status flag gets latched




Including the Flag Register in the System
=========================================



Programming with Conditional Jumps
==================================



For Next Time
=============

* Something?


