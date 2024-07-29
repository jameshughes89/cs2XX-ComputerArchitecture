*****************
Registers and RAM
*****************



Registers
=========


Storing a Byte
--------------



Random Access Memory
====================


Controlling Writes
------------------

With the decoder, one of the signals is always high, meaning at least one memory address will store whatever is on data in on clock pulses
However, we want more control on when to write

We use an enable, that will effectively toggle the decoder's decoded signal

COULD and with clock, but as discussed above with registers, this can cause issues



Controlling Reads
-----------------



For Next Time
=============

* Check out the :download:`1 bit register <1_bit_register.dig>` schematic for Digital
* Check out the :download:`1 byte register <8_bit_register.dig>` schematic for Digital
* Check out the :download:`RAM <4x4_ram.dig>` schematic for Digital
* Read Chapter 3 Section 6 of your text

    * 14 pages