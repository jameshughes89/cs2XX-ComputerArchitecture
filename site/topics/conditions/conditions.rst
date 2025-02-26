==========
Conditions
==========

* Although the system is programmable, it currently has a significant limitation
* To highlight this limitation, consider the problem the following problem

    * Given some number, output ``1`` if it is less than ``10``, otherwise, output ``0``


* It turns out that it's not possible as there is no way to check a condition

    * Think ``If`` statements



Conditional Jump Command
========================


Status Flags
------------



Flags Register
==============

Values from ALU always changing
    consider the fact that adding puts a value back into A, so the ALU's output even changes
    like 5 - 5 (- 5)

Need a way to preserve the flags
Use a register like before

When should the register be enabled? Only when doing an arithmatic operation


.. figure:: adder_flags_register.png
    :width: 666 px
    :align: center

    Configuration of an adder component with a status flag register. This design contains the logic to determine if any
    of the three status signals should be high based on the output of the adder. The value of the status signals can be
    latched into the flags register for later use.



For Next Time
=============

* Something?


