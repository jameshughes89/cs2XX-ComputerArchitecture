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



Enabling Flag Register
======================

* As discussed, the status flag register needs to be enabled at specific times to work

    * Only enable when performing addition or subtraction
    * Disabled at all other times


* However, both addition and subtraction take several clock cycles

    * Every instruction is allocated 4 clock cycles
    * Although, addition (``ADAB``) and subtraction (``SUAB``) only require 3

        * Fetch (2 clock cycles)
        * Output from ALU to the A register, and set the subtract signal where necessary (1 clock cycle)


* Therefore, the question is, when *exactly* should the flag enable signal be set high?

* It does not make sense to do it during the two clock cycles of fetch

    * All fetch cycles should be the same
    * Has nothing to do with the underlying instruction


* It could work during the ALU -> A register step

    * At this instant, the value the ALU has is the value to be calculated
    * Therefore, the status flags at this time are relevant to the instruction


* It would not work *after* the ALU -> A step

    * The value in the A register would be change after the ALU -> A step
    * This means the status flags may have changed
    * For example, performing ``5 - 5``

        * If A is ``5`` and B is ``5`` before subtraction, the ALU calculates ``0``, and the ``Z`` flag is high
        * After the ALU -> A step, A now stores ``0``, meaning the ALU calculates ``0 - 5``, and ``Z`` is now low


* Therefore, the flag register enable should be high at the time that the ALU is being output

.. note::

    One may wonder --- is it possible for the value from the ALU to be latched into A, thereby altering the status
    signals, before the value of the status signals can be latched into the flags register?

    This is not an unreasonable question to ask, and can be addressed by making the addition and subtraction
    instructions take four clock cycles by adding a new microinstruction after the fetch cycle, but before the ALU -> A
    step:

        * Fetch (2 cycles)
        * Set subtract if necessary and store the status signals (1 cycle)
        * Set subtract if necessary and ALU -> A (1 cycle)


    However, this is not a real concern given the synchronization of the system. Within Digital, values are latched into
    the registers the instant the clock signal goes high. In practice, there would be some delay due to the physical
    limitations of the hardware, but any delay on latching a value into the flags register would be less than the total
    delay of latching a value into the A register, outputting from the A register, moving to the ALU, and moving through
    the ALU.



Including the Flag Register in the System
=========================================



Programming with Conditional Jumps
==================================



For Next Time
=============

* Something?


