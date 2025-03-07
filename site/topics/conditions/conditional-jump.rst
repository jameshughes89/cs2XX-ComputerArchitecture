=============================
Conditional Jump Instructions
=============================

* The various status flag values can now be determined and stored in the flags register
* However, how should the conditional jumps be handled by the control logic?
* Further, the existing control logic needs to be updated to now handle the new flag register control signal

    * When should the system's status signal values be stored stored in the flags register?



Conditional Jump Control Logic
==============================

* The conditional jumps allow the program to jump to different parts of the program based on some condition
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


Controlling the Cases
---------------------

* If the status flags store their respective conditions, they indicate which version of the conditional jumps to perform

    * For example, if the :math:`Z_{flag}` signal is high, perform the jump version, if it's low, perform ``NOOP``


* The same idea used for dealing with the output register's unsigned/signed cases can be used

    * Multiple look up tables with a multiplexer *could* be used
    * Or, a single, larger, look up table with additional input signals can be used


* With this idea, the status flags can be input into the control logic's look up table

    * This results in a total of 9 inputs


.. figure:: control_logic_9_bit_input.png
    :width: 500 px
    :align: center

    The 9 bit input to the look up table broken down into the three parts --- flags, operator, and microcode counter.
    The most significant 3 bits, ``CSZ`` correspond to the status flags (carry, significant/sign, zero), the next 4 bits
    specify an instruction's operator ``XXXX``, and the final 2 bits ``YY`` are the microcode step, from the microcode
    counter.


* Like before, different segments of the input to the look up table have different meaning

    * The lest significant 2 bits correspond to the microcode counter
    * The next 4 bits correspond to the specific instruction
    * The additional 3 bits, the most significant bits, correspond to the status flags


.. figure:: control_logic_with_flags.png
    :width: 500 px
    :align: center

    Design of the look up table with the status flag signals included as inputs. This design has a total of 9 signals
    serving as inputs to the look up table --- 3 for the status signals, 4 for the instruction's operator, and 2 for
    the microcode step. Notice the ``FLG`` control signal on the output from the look up table --- this controls when
    the flags register is enabled.


* Since there are an additional 3 input bits, the size of the look up table grows by eight times

    * Eight segments of 16 instructions


* Each of the eight segments of the look up table corresponds to how the instructions should work given the status flags
* However, of the 16 instructions, only the 3 conditional jumps will be different, depending on the status flags

    * With this design, it means that there will be a lot of redundant, duplicate control logic
    * But it will make the implementation simple


* With this design in mind, there still needs to be control over when the flags register is enabled



Enabling Flag Register
======================



Including the Flag Register in the System
=========================================



Programming with Conditional Jumps
==================================



For Next Time
=============

* Something?


