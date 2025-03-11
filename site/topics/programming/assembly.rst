=================
Assembly Language
=================

* With the ability to make decisions, the ESAP system is now complete
* However, using the ESAP system is not particularly easy as it's programmed with machine code

    * Writing programs for the ESAP system is tedious
    * Machine code is prone to errors and and requires memorizing bit patterns


* A solution to this problem is to improve the way programming is done

    * Instead of binary patterns or hex numbers, english mnemonics can be used
    * Other quality of life features can be included, like separating opcode mnemonic from the operand value


* However, the ESAP system ultimately requires machine code



Assembler
=========




The ESAP Assembler
==================

* To make programming easier, a simple assembler will be built for the ESAP system
* This ESAP assembler will only implement the mnemonics and interpret various literal value encodings

    * It will not make use of labels for memory addresses


* The mnemonics make writing programs much easier
* It will also make interpreting/reading programs easier

    * ``LDAR 15`` versus ``0b00011111`` or ``0x1F``


* The mnemonics for each instruction have already been discussed in a previous topic

    * Below is a table of all 16 instructions
    * This table was shown before, but did not include the conditional jump instructions
    * These conditional jump instructions are included here


.. list-table:: Complete Instruction Set for the Current ESAP System
    :widths: auto
    :align: center
    :header-rows: 1

    * - Bit Pattern
      - Hex
      - Label
      - Description
    * - ``0000``
      - ``0``
      - ``NOOP``
      - No Operation
    * - ``0001``
      - ``1``
      - ``LDAR``
      - Load A From RAM
    * - ``0010``
      - ``2``
      - ``LDAD``
      - Load A Direct
    * - ``0011``
      - ``3``
      - ``LDBR``
      - Load B From RAM
    * - ``0100``
      - ``4``
      - ``LDBD``
      - Load B Direct
    * - ``0101``
      - ``5``
      - ``SAVA``
      - Save A to RAM
    * - ``0110``
      - ``6``
      - ``SAVB``
      - Save B to RAM
    * - ``0111``
      - ``7``
      - ``ADAB``
      - Add B to A --- ``A += B``
    * - ``1000``
      - ``8``
      - ``SUAB``
      - Subtract B from A --- ``A -= B``
    * - ``1001``
      - ``9``
      - ``JMPA``
      - Jump Always
    * - ``1010``
      - ``A``
      - ``JMPZ``
      - Jump if Zero Flag Set
    * - ``1011``
      - ``B``
      - ``JMPS``
      - Jump if Significant/Sign Flag Set
    * - ``1100``
      - ``C``
      - ``JMPC``
      - Jump if Carry Flag Set
    * - ``1101``
      - ``D``
      - ``OUTU``
      - Output Unsigned Integer
    * - ``1110``
      - ``E``
      - ``OUTS``
      - Output Signed Integer
    * - ``1111``
      - ``F``
      - ``HALT``
      - Halt


* The assembler will abel be able to translate literal from various bases

    * For example, the programmer could write ```0b1010``, ``10``, or ``0xA`` to mean ten
    * Although they all mean the same thing, one encoding may make more sense for the programmer in some context

        * Remember, code is for humans, machine code is for machines
        * An assembly language is one step away from machine code


* Negative numbers will also be handled

    * The assembler will convert the number to a two's complement number


* Finally, the ESAP assembler will provide some level of error checking on the program

    * Check if the program will fit into RAM
    * Syntax
    * Missing operands
    * Values within range


* Since an assembler is a program, a Python script can serve as the ESAP assembler
* Below, a script created for the ESAP system's assembler is discussed

    * This script is by no means the only way one could write an assembler


* A series of constants are used to simplify the code

    * A constant dictionary will be used for the mnemonic translation
    * Another constant set will keep track of which instruction requires an operand
    * Instruction syntax will be checked with a constant containing regex expressions

        * One expression for each instruction


.. literalinclude:: assembler.py
    :language: python
    :lineno-match:
    :start-after: # [begin-constants]
    :end-before: # [end-constants]


* Helper functions are also included that will make the assembly loop easier to implement


.. literalinclude:: assembler.py
    :language: python
    :lineno-match:
    :pyobject: parse_number


* The function ``parse_number`` interprets a string representing something can evaluates to a number to the number


.. literalinclude:: assembler.py
    :language: python
    :lineno-match:
    :pyobject: verify_number_and_fix_negative


* ``verify_number_and_fix_negative`` does two things

    * It verifies that a number can be represented with some specific number of bits

        * For example, if the number is data, it must fit in 8 bits
        * If the number is an operand, it must fit in 4 bits


    * This function also converts negative numbers to the integer representing the signed two's complement number

        * This is necessary as Python has a peculiarity when it comes to signed integers
        * Python stores signed integers as unsigned integers with a sign flag

            * It does not store the signed integers as two's complement numbers


        * For example ``-7`` would be stored as ``0b0111`` with a sign flag
        * However, the two's complement number for ``-7`` is ``0b1001``, which is what the ESAP system expects
        * This function would convert ``-7`` to the number representing the correct two's complement bit pattern
        * In this case, it would return the integer ``9``, which corresponds to the bit pattern ``0b1001``
        * Here, the value ``9`` is not important, but the underlying bit pattern for ``9`` is important



.. literalinclude:: assembler.py
    :language: python
    :lineno-match:
    :pyobject: verify_syntax_return_string


* The function ``verify_syntax_return_string`` checks that a given instruction is valid syntax

    * It checks that it matches one of the regular expressions defining each instruction's valid syntax


* The main part of the script uses the above constants and functions

.. literalinclude:: assembler.py
    :language: python
    :lineno-match:
    :start-after: # [begin-command_line_args]
    :end-before: # [end-command_line_args]


* The assembler takes one or two command line arguments

    * One argument specifies the name of the file containing the assembly code to assemble
    * The second argument, which is optional, specifies the name of the file to write the machine code to
    * This portion of the script verifies the a correct number of arguments are provided to the script


.. literalinclude:: assembler.py
    :language: python
    :lineno-match:
    :start-after: # [begin-read_assembly_file]
    :end-before: # [end-read_assembly_file]


* The assembler reads the assembly language code and verifies that it fits within RAM

    * It verifies that it is no more than 16 lines long
    * The assembler ignores blank lines

        * This means one must be careful not to assume that line number is the same as RAM address
        * This will be discussed in more detail in the next topic


* The main loop of the assembler processes one instruction at a time from the ``program_list`` variable

.. literalinclude:: assembler.py
    :language: python
    :lineno-match:
    :start-after: # [begin-process_each_instruction]
    :end-before: # [end-process_each_instruction]


* The main loop verifies the line and processes it as an instruction or data accordingly

    * If it's an instruction, it processes the operand if necessary too


* Finally, the assembler saves the assembled code to a file

.. literalinclude:: assembler.py
    :language: python
    :lineno-match:
    :start-after: # [begin-save_to_file]
    :end-before: # [end-save_to_file]


* Using the assembler is then a matter of running the script with the proper command line arguments

    * For example, ``python assembler.py to_assemble.esap assembled.hex``
    * The file extension ``.esap`` is not necessary for the assembly language file
    * If the second argument is not set, the file is saved to ``a.hex`` by default



For Next Time
=============

* Something?


