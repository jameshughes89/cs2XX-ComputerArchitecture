=============================
Conditional Jump Instructions
=============================

* The various status flag values can now be determined and stored in the flags register
* However, how should the conditional jumps be handled by the control logic?
* Further, the existing control logic needs to be updated to now handle the new flag register control signal

    * When should the system's status signal values be stored stored in the flags register?



Conditional Jump Control Logic
==============================

* The conditional jumps allow the program to to different parts of the program based on some condition
* More specifically, when some status flag is high, the conditional jump updates the program counter's value

    * The program counter is updated to contain a new memory address --- the address of the new next instruction
    * In the same way as the jump always instruction


* For example, consider a jump zero command --- ``JMPZ``

    * If the zero status flag is high, update the program counter with some specified memory address
    * If the status flag is low, ignore and carry on


* Notice that this instruction has two cases

    * Two versions of the instruction that can be performed


* The control logic for the two versions of the instruction effectively already exists

    * The jump version control logic is the same as the ``JMPA`` instruction

        * Fetch cycle
        * Move operand (memory address to jump to) out from the instruction register into the program counter

    * The ignore version is a ``NOOP``

        * Fetch cycle
        * Nothing


* What does not exist is a way to select which version of the instruction to perform

    * The jump, or the ``NOOP`` version






How can it know?
Use the same idea as the signed control signal
    when the flag is off, do NOOP
    when the flag is on, do jump


Discussed in more details below, but it really is the same idea as the output register
    could have a multiplexer and multiple LUTs
    or we could have additional inputs to the LUT specifying chunks of the LUT for the various cases
    this means we will have 8x the size of the LUT though


Ok, so we also need to control the status flags


Enabling Flag Register
======================



Including the Flag Register in the System
=========================================



Programming with Conditional Jumps
==================================



For Next Time
=============

* Something?


