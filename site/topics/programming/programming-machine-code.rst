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

* Now consider the problem of outputting all the positive integers, starting from ``0``

* Python code for this would be something like this

    .. code-block:: python
        :linenos:

        count = 0
        while True:
            print(count)
            count += 1


* Considering the instructions available, the same idea can be achieved with the following pseudocode

    #. Load ``0`` into register A
    #. Load ``1`` into register B
    #. Save register A's value to RAM
    #. Output the saved value
    #. Perform addition
    #. Jump to instruction 3


* The load direct instructions can be used because the initial values can fit within 4 bits

    * This eliminates the need for an additional memory location to store the data to be loaded


* The current value of A is displayed by first saving it to RAM, and then outputting it as an unsigned integer

    * To keep the data seperated from the instructions in RAM, address ``0xF`` will be used


* Addition adds the value in register B (``1``) to the current value stored in register A

    * ``A += B``
    * Or, more specifically here, ``A += 1`` since B is always ``1``


* Finally, the program must loop

    * A jump instruction is used to go to the address saving the value of register A for output
    * The operand of the jump command is the memory address of the instruction to jump to


* The complete machine code program is as follows

    .. code-block:: text
        :linenos:

        v2.0 raw
        0x20
        0x41
        0x5F
        0xDF
        0x70
        0x92
        0x00
        0x00
        0x00
        0x00
        0x00
        0x00
        0x00
        0x00
        0x00
        0x00


Analysis
--------

* Notice that this program has no ``HALT``
* What will happen when the counted value reaches ``255``?

    * The result of ``0b11111111 + 1`` is ``0b1_00000000``, which is 9 bits
    * This means the carry bit on the adder will go high, but the 8 bit output of the adder would be ``0b00000000``
    * This 8 bit ``0b00000000`` would be saved to register A
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


