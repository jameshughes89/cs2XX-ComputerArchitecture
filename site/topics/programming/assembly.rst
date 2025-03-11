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
      - Jump Zero
    * - ``1011``
      - ``B``
      - ``JMPS``
      - Jump Significant/Sign
    * - ``1100``
      - ``C``
      - ``JMPC``
      - Jump Carry
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



It relaly is a simple program

show program in bits

    constants
    functions?

    error checking
    loading and error checking 
    while thing



For Next Time
=============

* Something?


