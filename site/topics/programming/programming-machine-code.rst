=============================
Programming with Machine Code
=============================

* The ESAP system now has a way to manipulate its own control logic
* With this, it can be programmed and execute the program automatically on itself
* In other words, it's now possible to write instructions into RAM and have the computer execute the program



Arithmetic Program
==================

* Consider the simple problem of adding and subtracting some numbers and outputting the results
* For example

    * Output the result of 31 + 32
    * Output the result of 31 - 32


* In a language like Python, this program would simply be

    .. code-block:: python
        :linenos:

        print(31 + 32)
        print(31 - 32)


* The instructions available to the ESAP system are much more limited
* However, this can still be programmed into the system with the instruction set available

    * Although possible, there will be more steps involved


* The process of coming up with the program is the same as Python or other high level languages

    * Break the problem down into small parts that can be calculated one step at a time


* For this arithmetic problem, here is a pseudocode like breakdown of a solution to the problem

    #. Load ``31`` into register A
    #. Load ``32`` into register B
    #. Perform addition
    #. Save the result to RAM
    #. Output the result
    #. Load ``31`` into register A
    #. Load ``32`` into register B (not a necessary step as ``32`` is already in register B)
    #. Perform subtraction
    #. Save the result to RAM
    #. Output the result
    #. Halt


* Now it's a matter of converting these instructions into the machine code


Loading Data into the Registers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* There are two options for this --- load from RAM or direct

    * Load from RAM --- ``LDAR``/``LDBR``
    * Load direct --- ``LDAD``/``LDBD``


* However, since the values to be loaded into the registers are beyond 4 bits, loading from RAM is required
* Therefore, the operator would be

    * ``LDAR`` --- ``0b0001``/``0x1``
    * ``LDBR`` --- ``0b0011``/``0x3``

* This means that these numbers are stored somewhere in RAM
* The RAM addresses of these numbers would be the operands of these instructions


* Where to store the ``31`` and ``32``?

    * It does not really matter where the numbers are stored in RAM as long as the addresses are available
    * In a Von Neumann architecture based system, which this is, instructions and data share the same memory space
    * However, it is still common to separate instructions and data where possible
    * For this reason, the data will be stored in addresses near the end of RAM

        * ``0b1110``/``0xE`` will store ``31``
        * ``0b1111``/``0xF`` will store ``32``


* Therefore, the first two machine code instructions are

    * The data values stored in the last two addresses are excluded from here

    .. code-block:: text
        :linenos:

        v2.0 raw
        0x1E
        0x3F


.. note::

    Because the programs are written in a hex file format, ``v2.0 raw`` is required for the file to be parsed correctly
    by Digital.

    Additionally, one could have used different number bases to write the code, like binary:

        * ``0b00011110``
        * ``0b00111111``


    Here, the hex numbers are used for brevity and simplicity.


Addition and Outputting
^^^^^^^^^^^^^^^^^^^^^^^

* Addition stores the result in register A, overwriting what was stored in it before

    * ``ADAB`` --- ``0b0111``/``0x7``
    * Addition takes no operand, so its value is ignored

        * This means any 4 bit value can be the operand, but to keep the code clean the operand should be ``0``


* The result of addition, that was placed into register A, needs to be saved to RAM before it can be output

    * ``SAVA`` --- ``0b0101``/``0x5``
    * The operand for this instruction specifies the RAM address to save the contents of register A to

        * Any available RAM address can be used, but to keep things seperated, address ``0b1100``/``0xC``


* The output instructions send data from RAM to the output register

    * There are two possible instructions for outputting data

        * Output unsigned integer --- ``OUTU`` --- ``0b1101``/``0xD``
        * Output signed integer --- ``OUTS`` --- ``0b1110``/``0xE``


    * Either would work in this particular case since the sum (``63``) is small enough

        * The 8 bit unsigned/signed patterns are the same for this number


    * However, to keep code clean and intentional, ``OUTU`` would be preferred
    * The operand for this instruction specifies the RAM address' contents to output

        * Here, that would be ``0b1100``/``0xC``


* Therefore, the machine code instructions would now include

    .. code-block:: text
        :linenos:

        v2.0 raw
        0x1E
        0x3F
        0x70
        0x5C
        0xDC


Subtraction, Outputting, and Halting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The data will be re-loaded into the registers

    * The value ``31`` must be put back into register A as it was overwritten by the ``ADAB`` instruction
    * The value ``32`` does not need to be placed into register B as it is already there

        * However, to keep the code clear, the instruction will be run again
        * Although, this does come at the cost of additional clock cycles and RAM


* Similar to addition, subtraction overwrites the contents of the A register

    * ``SUAB`` --- ``0b1000``/``0x8``
    * Subtraction takes no operand, so ``0`` will be used


* The result of subtraction needs to be saved to RAM before it can be output

    * ``SAVA`` --- ``0b0101``/``0x5``
    * The RAM address (operand) will be ``0b1101``/``0xD``

        * This follows the address the result of the addition was stored in


* Since the result of subtraction should be a negative number (``-1``), the signed output instruction should be used

    * ``OUTS`` --- ``0b1110``/``0xE``
    * The operand would be the address of the value to be output --- ``0b1101``/``0xD``


* Finally, the program needs to stop running

    * ``HALT`` --- ``0b1111``/``0xF``
    * No operand is needed


* The complete machine code program is as follows

    .. code-block:: text
        :linenos:

        v2.0 raw
        0x1E
        0x3F
        0x70
        0x5C
        0xDC
        0x1E
        0x3F
        0x80
        0x5D
        0xED
        0xF0
        0x00
        0x00
        0x00
        0x1F
        0x20


* Since each line corresponds to one RAM address, each line should be filled
* However, before runtime, the contents of addresses ``0xB``, ``0xC``, and ``0xD`` are not used

    * Although, ``0xC`` and ``0xD`` are written to by the program at runtime


* Because a ``HALT`` exists in address ``0xA``, these unused addresses can never be executed by the system
* Therefore, the contents of these RAM address don't actually matter
* However, to keep the code clean ``NOOP``/``0x0`` will be put in these addresses


Analysis
^^^^^^^^

* Consider the resources this program uses

    * Both in terms of time (clock cycles) and space (RAM)


* How many clock cycles does the program take?

    * There are a total of 11 instructions
    * Each instruction takes 4 microcode steps
    * Therefore, a total of :math:`11 \times 4 = 44`` clock cycles

        * Technically it's :math:`43`` as ``HALT`` will stop the whole system after its 3rd clock cycle
        * ``HALT`` only requires 3 clock cycles, not the full 4


* Can the program be adjusted to take fewer clock cycles?

    * The instruction to re-load ``32`` into register B for subtraction was unnecessary
    * This would save 4 clock cycles

        * This may not feel like a lot, but that's roughly :math:`9.1\%` of the execution time of the whole program


.. admonition:: Activity

    Could something about the system be changed to reduce the total number of clock cycles?



* Currently the program takes up 15 memory addresses

    * 11 instructions
    * 2 addresses with data
    * 2 more addresses are used to store data at runtime


* This can be reduced to 12 by

    * Removing the instruction to re-load ``32`` into register B will save 1 RAM address for the instructions
    * The result of subtraction could have been saved to the same address as addition, saving 1 runtime address
    * The results of add/sub could have overwritten the value ``32`` in address ``0xF``, saving another address


Halting
^^^^^^^

* Consider the program before improving the required clock cycles and RAM requirements
* What would happen if the ``HALT`` instruction was not included in this program and had another ``NOOP`` instead?

    * The system would process and execute the ``NOOP``\s in address ``0xA`` and ``0xB``
    * Each ``NOOP`` would take 4 clock cycles before moving on to the following instruction


* However, the remaining memory address have data stored in them

    * ``0xC`` stores the result of addition calculated at runtime --- ``63``, which is ``0x3F``
    * ``0xD`` stores the result of subtraction calculated at runtime --- ``-1``, which is ``0xFF``
    * ``0xE`` stores a number --- ``31``, which is ``0x1F``
    * ``0xF`` stores a number --- ``32``, which is ``0x20``


* Although we know the contents of these memory addresses is data, the system does not know the difference
* As far as the system is concerned, these are instructions to be processed

    * Address ``0xC`` --- ``LDBR`` the contents of address ``0xF``
    * Address ``0xD`` --- ``HALT``
    * Address ``0xE`` --- ``LDAR`` the contents of address ``0xF``
    * Address ``0xF`` --- ``LDAD`` the value ``0x0``


* Therefore, the system would execute the data as if they were instructions

    * The program would halt after hitting address ``0xD`` through pure luck
    * However, it should be clear that this is something to be very mindful of


.. warning::

    When using the ``SAVA`` instruction, an effort was made to save to memory addresses away from instructions, keeping
    a separation between instructions and data. However, this is not a requirement, and any memory address could have
    been written to.

    If one wanted, they could write data to an address that stores an instruction, thereby overwriting it. This means
    that the program can modify its own code at runtime, changing the instructions to be executed by the system.

    Is this something one should do? I this a good idea?



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


