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

* It does not make sense to do it during the two clock cycles of fetch

    * All fetch cycles should be the same
    * Has nothing to do with the underlying instruction


* It could work during the ALU -> A register step
* It would not work *after* the ALU -> A step

    * The value in the A register would be change after the ALU -> A step
    * This means the status flags may have changed
    * For example, performing ``5 - 5``

        * If A is ``5`` and B is ``5`` before subtraction, the ALU calculates ``0``, and the ``Z`` flag is high
        * After the ALU -> A step, A now stores ``0``, meaning the ALU calculates ``0 - 5``, and ``Z`` is now low


* Therefore, the flag register enable should be high at the time that the ALU is being output

.. note::

    One may wonder --- is it possible for the value from the ALU to be latched into A, thereby altering the status
    signals before the value of the status signals can be latched into the flags register?

    This is not an unreasonable question to ask, and can be addressed by making the addition and subtraction
    instructions take four clock cycles by adding a new step after the fetch cycle, but before the ALU -> A step:

        * Fetch (2 cycles)
        * Set subtract if necessary and store the status signals (1 cycle)
        * Set subtract if necessary and ALU -> A (1 cycle)


    However, this is not a real concern given the synchronization of the system. Within Digital, values are latched into
    the registers the instant the clock signal goes high. In practice, there would be some delay due to the physical
    limitations of the hardware, but any delay on latching a value into the flags register would be less than the total
    delay of latching a value into the A register, outputting from the A register, moving to the ALU, and moving through
    the ALU.



Including the Flag Register in the System
=========================================



Programming with Conditional Jumps
==================================



For Next Time
=============

* Something?


