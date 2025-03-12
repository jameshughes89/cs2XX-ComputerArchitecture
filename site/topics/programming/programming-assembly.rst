=========================
Programming with Assembly
=========================

* With the use of an assembler, generating the machine code for the ESAP system becomes easier
* Once the assembly language is written, it can be *assembled* into the machine code, that can be loaded into RAM



Arithmetic Program
==================



Counting Program
================



Count to 10
===========

cleary assembler makes it easier
juggling the complexity of machine code and complex problems is hard
with the assembler, now it's much easier
consider a more vomplex problem combining some of the above ideas
count to 10, then stop

    1 -- 10


loop, but branching

Below is the code

    .. list-table:: Count to 10
        :header-rows: 1
        :align: center

        * - Assembly
          - Machine Code

        * - .. literalinclude:: counting_10.esap
                :language: text
                :lineno-match:

          - .. literalinclude:: counting_10.hex
                :language: text
                :lineno-match:



here, the jump S is used to loop
notice the storing of the value before doing sub 10

When running, it will appear that it counts 0 -- 10, but only because output reg starts at 0



For Next Time
=============

* Something?


