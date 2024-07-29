*****************
Registers and RAM
*****************



Registers
=========


Storing a Byte
--------------

* A D flip-flop with enable can act as a register to effectively store a single bit of information
* To store more than a single bit, configure multiple registers in parallel
* For example, to store 8 bits/1 byte of data, stack eight registers together

.. figure:: 8_bit_register.png
    :width: 333 px
    :align: center

    Eight D flip-flops with enables (registers) configured in parallel such that they can store eight bits/one byte of
    information. A single :math:`EN` signal controls when all bits are stored in the register.


Random Access Memory
====================


Controlling Writes
------------------


Controlling Reads
-----------------



For Next Time
=============

* Check out the :download:`1 bit register <1_bit_register.dig>` schematic for Digital
* Check out the :download:`1 byte register <8_bit_register.dig>` schematic for Digital
* Check out the :download:`RAM <4x4_ram.dig>` schematic for Digital
* Read Chapter 3 Section 6 of your text

    * 14 pages