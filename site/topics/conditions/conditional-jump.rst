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


* This problem can be solved with the following general idea

    * Load value into register A
    * Subtract ``10`` from the value

        * If the result is negative (the most significant bit is high), the value must be ``< 10``


    * If the result is negative, jump to a a part of RAM that outputs ``1``

        * ``JMPS``


    * If the result is not negative, output ``0``


* Below is the ESAP system's machine code for the above idea

    * The emphasized line contains the conditional jump for the significant bit/sign flag
    * Here, the value in RAM address 15 is the number to check

.. literalinclude:: check_10.hex
    :language: text
    :lineno-match:
    :emphasize-lines: 5


* To make this more human readable, the program is

    0. Load the value from address 15 to register A
    1. Load the value 10 to register B
    2. Calculate the difference
    3. Jump to address 6 if the significant bit/sign flag is high
    4. Output the contents of register 13
    5. Halt
    6. Output the contents of register 14
    7. Halt
    8. ``NOOP``
    9. ``NOOP``
    10. ``NOOP``
    11. ``NOOP``
    12. ``NOOP``
    13. 0
    14. 1
    15. Number to check





now we can do like a while loop
Count to 10





For Next Time
=============

* Something?


