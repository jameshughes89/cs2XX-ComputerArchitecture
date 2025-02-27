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

.. figure:: status_flags_observing_alu.png
    :width: 500 px
    :align: center

    Status flag signals connected to an ALU. The output of the ALU would typically be sent back to the data bus, but
    here the output is ignored except for analysing the output's status for the purpose of determining the status flags.


* The goal is to know if the last arithmatic operation performed caused any of the status signals to change
* However, the adder is always outputting a value based on the contents of registers A and B

    * This is true, even when addition/subtraction is not being performed


* For example, consider the steps the system performs when performing ``5 - 5``

    * Load data into A
    * Load data into B

        * At this instant, the status flag signal for ``0`` should be high

            * The overflow will also be high too, as a consequence of 2s compliment


    * Put value from ALU into A

        * At this instant, the status flag for ``0`` will be high
        * This is because the adder always calculates the sum/difference of the values in registers A and B
        * Therefore, since the ALU is outputting ``-5``, the zero flag is low, but the significant/sign flag is high


.. figure:: status_flags_5_minus_5_before_data_to_a.png
    :width: 500 px
    :align: center

    Status flag signals after the ALU calculates ``5 - 5``, but before the output of the ALU is sent back into register
    A. Notice that the zerp flag is high, since ``5 - 5 = 0``.


.. figure:: status_flags_5_minus_5_after_data_to_a.png
    :width: 500 px
    :align: center

    Status flag signal after the result of ``5 - 5`` (``0``) is placed into register A. Since the ALU is always
    calculating the difference of the current values in registers A and B, the value being output by the adder component
    will be ``(5 - 5) - 5``, or ``-5``. Because of this, the zero flag is no longer high, even though the last operation
    that was intended did in fact result in a zero.



This is a problem since we need to know the status flag after the last thing we actually cared about D:

Need a way to preserve the flags
Use a register like before

When should the register be enabled? Only when doing an arithmatic operation


* Below is an example of an adder with logic for the status flag signals being fed into a flag register

    * Here, except for the status flags logic, the value of the output of the adder is ignored


.. figure:: adder_flags_register.png
    :width: 666 px
    :align: center

    Configuration of an adder component with a status flag register. This design contains the logic to determine if any
    of the three status signals should be high based on the output of the adder. The value of the status signals can be
    latched into the flags register for later use.



For Next Time
=============

* Something?


