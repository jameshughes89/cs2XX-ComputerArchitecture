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


* Consider the more complex problem of counting to 10

    * Output the numbers ``1`` to ``10``
    * This may sound simple, but it is challenging when programming at such a low level


* This problem combines two of the previous problems

    * Counting forever

        * requires looping


    * Checking if a value is less than 10

        * requires branching


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


* Notice how the count value must be preserved before the subtraction can happen
* Here, the ``JMPS`` instruction is used like a kind of while loop

    * While the count is less than 10, jump


* Note that, when running the program, it will appear to count ``0`` -- ``10``

    * This is due to the simulator and how the output register starts with a ``0``


* Additionally, the starting instructions of ``LDAD 0`` and ``SAVA 0xF`` could have been excluded

    * The simulator initializes RAM with ``0``\s
    * However, having clear and intentional code is preferred



For Next Time
=============

* Something?


