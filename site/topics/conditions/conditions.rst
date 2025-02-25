==========
Conditions
==========

* Although the system is programmable, it currently has a significant limitation
* To highlight this limitation, consider the problem the following problem

    * Given some number, output ``1`` if it is less than ``10``, otherwise, output ``0``


* It turns out that it's not possible as there is no way to check a condition

    * Think ``If`` statements



Conditional Jump Command
========================

* Consider the general idea of the program

    * Load value into register A
    * If register A's value is ``< 10``

        * Output ``1``
        * Halt


    * Otherwise

        * Output ``0``
        * ``Halt``


* Currently there is no way to have a program branch based on a condition

    * There is no ``if`` style instruction


* However, the current instruction set does include a jump instruction, which does provide some way to move around RAM
* Therefore, using the idea of a jump, the program can be reframed

    * Load value into register A
    * If register A's value is ``< 10``, jump to a part of RAM containing the following instruction

        * Output ``1``
        * Halt


    * Otherwise

        * Output ``0``
        * ``Halt``


    .. code-block:: text
        :linenos:

        v2.0 raw
        0x1F (load data from address 0xF into A)
        0x?4 (Jump to address 0x4 if < 10)
        0xDD (Output 0)
        0xF0 (Halt)
        0xDE (Output 1)
        0xF0 (Halt)
        0x00
        0x00
        0x00
        0x00
        0x00
        0x00
        0x00
        0x00 (0 to output if not < 10)
        0x01 (1 to output if < 10)
        0x?? (some number to check)


* Unfortunately, the jump instruction available in the current instruction set *always* jumps

    * There is no condition


* However, there is room to add to the instruction set
* Therefore, consider how this conditional jump idea *could* be done

    * What should the condition be?
    * How should the system handle it?


* Having a jump for a specific condition and value like ``< 10`` is not particularly general
* Instead, one could checks for ``== 0`` or ``< 0`` as they are far more general and useful

    * For example, if one wants to check if some value is ``< 10``, simply check the difference

        * If ``(value - 10) < 0``, then ``value < 10``


TURNS OUT WE REALLY ONLY NEED 1 CONDITION 




idea of a jump, but only under certain conditions
so, behaviors of the jump needs to change depending on the state of the sytem
for example, if things are equal
    result of operation was 0

We could check if a given value is something
    or after some operation


remembering back the ALU, there were status out

Technically we only need 1 type of condition, but to make things more flexible, it's good to have a few
    zero
    carry
    sign


But.... how do we know? How to check


Status Flags
------------

zero is easy --- are all bits in a number 8?
what about sign?
what about carry?

SHOW IMAGE OF DESIGN



Flags Register
==============




For Next Time
=============

* Something?


