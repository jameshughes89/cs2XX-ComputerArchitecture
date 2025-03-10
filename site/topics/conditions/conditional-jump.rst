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



Programming with Conditional Jumps
==================================

* With this new functionality, conditional jumps, branching can now be achieved


* Consider the problem discussed before

    * Given some number, output ``1`` if it is less than ``10``, otherwise, output ``0``


* This problem can be solved with the following general program idea

    * Load value into register A
    * Subtract ``10`` from the value

        * If the result is negative (the most significant bit is high), the value must be ``< 10``


    * If the result is negative, jump to a a part of RAM that outputs ``1``

        * ``JMPS``


    * If the result is not negative, output ``0``







show program
this is more of a branch idea


now we can do like a while loop
Count to 10





For Next Time
=============

* Something?


