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

* How many clock cycles will this take?

    11 * 4 (though, halt actually stops after 3)
    eliminate the loading 32 saves 4 clock cycles
    THINK OF THE SPEED UP
        %?

* how much RAM does this take?

    Can make less
    Can over write result of addition
    Can over write the 32 actually!


* What happens if we do not HALT?

    Address C has 63 in it (0x3F) Load contents of F into reg B? (lol)
        oh my, we gotta be careful

    Address D has -1 in it (0xFF)
    * 31 is 1F (load A contents F)
    * 32 is 20 (Load A direct 0)


Counting Program
================



For Next Time
=============

* Something?


