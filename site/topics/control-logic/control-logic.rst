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



Look Up Table to Process Instruction
====================================

could do each by hand, many signals
and 16 instructions x 4 microcodes ecah is tedius

thus, a script will be made like the seven segment display to programatically do it

CONSTANTS

so, this means the signal hooked up to most sig bit is HLT for halt

note that the order of the control logic does not matter
the chouce of the order here is for the design of the control signals
all that really matters is that each signal hooks up to the corresponding module in the system

LIST OF INSTRUCTIONS

Talk about them

Write to file





Including the Control Logic Module in the System
================================================



For Next Time
=============

* Something?


