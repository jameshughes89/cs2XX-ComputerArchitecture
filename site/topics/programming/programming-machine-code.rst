=============================
Programming with Machine Code
=============================

* The ESAP system now has a way to manipulate its own control logic
* With this, it can be programmed and execute the program automatically on itself
* In other words, it's now possible to write instructions into RAM and have the computer execute the program



Arithmetic Program
==================



Counting Program
================

Explain program

explain it in instructions

can use direct loads

jump to 2

    B already has 1
    A was overwritten by the incremented value (last addition)


SHOW PROGRAM


Analysis
--------

* Notice that this program has no ``HALT``
* What will happen when the counted value reaches ``255``?

    * The result of ``0b11111111 + 1`` is ``0b1_00000000``, which is 9 bits
    * This means the carry bit on the adder will go high, but the 8 bit output of the adder would be ``0b00000000``
    * In other words, the counted value would loop back to ``0`` before carrying on


* Since this program never halts, it could run forever

    * It would run until it's turned off by something external to the system
    * The number of clock cycles is effectively infinite


* The amount of RAM this program takes up is 7 addresses

    * 6 instructions
    * 1 address used to store data at runtime for outputting



For Next Time
=============

* Something?


