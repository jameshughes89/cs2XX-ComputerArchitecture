=============
Control Logic
=============

* Instructions are fetched and put into the instruction register for processing

    * An instruction set has already been defined
    * Each instruction's microcodes are known

        * How the hardware is manipulated for each instruction


* However, there is still no way for the system to manipulate its own control logic

    * There is no way for the system to take an instruction and then activate/deactivate the various hardware modules


* In other words, how can the system know how to physically perform an instruction



Instruction and Microcode Steps
===============================

Consider the instruction register

IMAGE

most sig bits are the instruction
least sig bits are the operand, and as discussed, are important for many operations
    consider LDAR
    thus, it goes back to RAM


But the operand means we need to do some series of steps
    use LDAR again

A look up table would be good, except we need several steps

So, let's make a new counter

    Show table example


SHOW IMAGE

Notice that table still follows binary count!


A matter of compleeting the table for every instruction



Look Up Table to Process Instruction
====================================



Including the Control Logic Module in the System
================================================



For Next Time
=============

* Something?


