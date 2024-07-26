*****************
Registers and RAM
*****************

* D flip-flops allow one to store a single bit of information
* However, they always update what's stored on every clock pulse
* In many cases, one wants more control over *when* the stored data in the D flip-flop is updated



Registers
=========

* D flip-flops have several uses, but they always update the stored value every time the clock pulses

    * If the data line is low, then the D flip-flop will store a ``0`` on a clock pulse
    * If the data line is high, then a ``1`` is stored on a clock pulse


* However, for general purpose memory, the goal is to leave the stored data alone for several clock cycles
* In other words, there needs to be a way to toggle when the signal on the data line is to be stored on a clock pulse

    * When enabled, store the data on the data line when the clock pulses
    * When not enabled, ignore the data on the data line and leave the stored data unchanged when the clock pulses


* One way this can be achieved is to still update the stored value on every clock pulse
* However, it will update to either

    * The value on the data line
    * The value that is already stored


* This means there will effectively be two data lines

    * The actual data line
    * A feedback line from the D flip-flop's output


* Then, all that is needed is a multiplexer to toggle between which of the two data lines should be read form


.. figure:: 1_bit_register.png
    :width: 500 px
    :align: center

    A D flip-flop with enable, which can be used as a register. When the :math:`EN` signal is low, the multiplexer
    selects the :math:`Q` signal, meaning the value of :math:`Q` will be fed back into the D flip-flop, which will be
    re-latched on a clock pulse, leaving the value stored effectively unchanged. When :math:`EN` is high, the value from
    the :math:`D` line will be latched on a clock pulse.


* This type of structure is called a D flip-flop with enable, and can be used as a *register*

    * For registers, it is common to ignore :math:`\lnot Q`


* The two data lines are

    * :math:`D` --- the actual data line
    * :math:`Q` --- the output of the D flip-flop


* The multiplexer in front of the D flip-flop allows for selecting which data line's signal is stored

* When :math:`EN` is low

    * The multiplexer selects the :math:`Q` line
    * The value of :math:`D` is ignored
    * The value of :math:`Q`, whatever it is, will be re-latched into the D flip-flop on a clock pulse
    * The value stored in the register is effectively unchanged


* When :math:`EN` is high

    * The multiplexer selects the :math:`D` line
    * The value of :math:`Q` is ignored
    * The value of :math:`D`, whatever it is, is latched into the D flip-flop on a clock pulse
    * The value stored in the register is updated


.. note::

    One may wonder, why go through the trouble of using a multiplexer and feeding the output :math:`Q` back into the
    circuit when one could simply AND the clock signal with the enable signal? If this were the case, when :math:`EN` is
    low, no clock pulse will reach the D flip-flop, when :math:`EN` is high, clock pulses can pass through the AND gate.
    In other words, this simpler design would function perfectly as a D flip-flop with enable.

    One could absolutely do this; however, in practice, although this *can* work, it would cause a slight delay in the
    clock signal which could cause problems. Usually, it's a good idea to leave the clock signal alone.



Storing a Byte
--------------



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