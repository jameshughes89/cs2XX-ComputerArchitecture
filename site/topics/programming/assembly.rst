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

* An assembly language is a very low level programming language

    * Often referred to as *assembly*


* When compared to machine code, it enables a more human centric way of programming the system
* Assembly languages have many benefits over programming in machine code, but two key important features are

    * Mnemonics for referring to specific instructions

        * For example, consider loading the value 5 into register A
        * Instead of the machine code ``0b00100101``, one could write ``LDAD 5``
        * The mnemonic would mean the same thing, and would be translated to the machine code
        * But the mnemonic is much easier to remember and mentally parse


    * Labels/symbolic representation for memory addresses

        * For example, memory addresses could be labelled
        * This would make referencing memory addresses for jumps and loading from RAM easier
        * Removes the need to remember specific memory addresses
        * Also removes the need to constantly update addresses when lines are added/removed to RAM




* However, it is strongly tied to a specific system design, the underlying hardware, and its machine language
* Typically, each statement in assembly has a 1-to-1 mapping to a statement in machine code



Many features, but 2 big ones are
    nmonics
    labels


Still limted though


* An assembler is a tool used to translate, or *assemble* assembly language to machine code
* Kinda like compilers for high level programming languages


The ESAP Assembler
==================



For Next Time
=============

* Something?


