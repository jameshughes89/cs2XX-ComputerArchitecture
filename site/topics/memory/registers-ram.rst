*****************
Registers and RAM
*****************



Registers
=========


Storing a Byte
--------------



Random Access Memory
====================

* Without knowing how to actually store data, the high level idea of RAM was previously discussed

.. figure:: 4x4_memory_with_plexers.png
    :width: 750 px
    :align: center

    Visualization of an incomplete 4x4 block of RAM.


* To review, above is a 4x4 block of RAM

    * There are four 4 bit memory addresses


* A decoder is used to select which memory address is active

    * Notice how the decoded line activates all bits within a memory address


* Multiplexers are used to relay the stored data out from the selected memory address

    * Notice that there is a multiplexer for each of the four bits in the memory addresses


* Since registers (D flip-flops with enable) can be used to store data, they can be used for building RAM




SHOW IMAGE



Same idea as above, but
Add a clock
Added controllable inputs
    data in
    addresses

A way to contorl writes
a way to control reads


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