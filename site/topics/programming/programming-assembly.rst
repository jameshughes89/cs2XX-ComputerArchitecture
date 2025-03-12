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

* With the use of the assembler, the programs are easier to write and understand
* This is important as solving complex problems is challenging enough as is

    * The tedium of machine code only makes solving complex problems that much more difficult


* Since an assembler exists for the ESAP system, consider the more complex problem of counting to 10

    * Output the numbers ``1`` to ``10``
    * This may sound simple, but it is challenging when programming at such a low level


* This problem combines two of the previous problems

    * Counting forever

        * Required looping


    * Checking if a value is less than 10

        * Required branching


* Below is the assembly and corresponding machine code for a solution to this problem

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


