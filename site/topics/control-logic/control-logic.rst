=============
Control Logic
=============

* Instructions are fetched and put into the instruction register for processing

    * An instruction set has already been defined
    * Each instruction's microcodes are known

        * How the hardware is manipulated for each instruction


* However, there is still no way for the system to manipulate its own control logic

    * There is no way for the system to take an instruction and then activate/deactivate the various hardware modules


* In other words, how can the system know how to physically perform an instruction?



Instruction and Microcode Steps
===============================

.. figure:: instruction_register.png
    :width: 500 px
    :align: center

    The instruction register stores the operator and operand of the current instruction. The operand is output to the
    bus for use during the execution of the instruction. The operator remains in the resister for processing.


* Consider what is stored in the instruction register and what is being output

    * The operator, specifying some instruction to execute

        * The most significant four bits in the instruction


    * The operand, specifying some data for use in execution of the specific instruction

        * The least significant four bits in the instruction


* As previously discussed, each instruction requires several steps

    * For example, loading data into register A from RAM (``LDAR/0001``)

        * Output the operand from the instruction register and put it into the address register
        * Output the value from the specified RAM address to the A register


* Additionally, before any processing of any instruction can occur, it must be fetched from RAM

    * In other words, no matter what instruction is to be executed, it must be fetched from RAM


* In other words, any one instruction requires several steps


Microcode Counter
-----------------

* The operator can be used to specify the steps to be executed in order to perform the instruction
* Thus, a look up table can be used to find the steps required to perform the full instruction
* However, there is a problem with this idea since instruction may require several sequential steps too complete

    * Consider the below table of the 4 steps required for loading data from RAM to register A


.. list-table:: Full control logic of ``LDAR``
    :widths: auto
    :align: center
    :header-rows: 1

    * - :math:`Address`
      - :math:`RAM`
      - :math:`A`
      - :math:`B`
      - :math:`ALU`
      - :math:`out`
      - :math:`PC`
      - :math:`Instruction`
    * - ``1``
      - ``0/0``
      - ``0/0``
      - ``0/0``
      - ``0/0``
      - ``0/0``
      - ``0/1/0``
      - ``0/0``
    * - ``0``
      - ``0/1``
      - ``0/0``
      - ``0/0``
      - ``0/0``
      - ``0/0``
      - ``0/0/1``
      - ``1/0``
    * - ``1``
      - ``0/0``
      - ``0/0``
      - ``0/0``
      - ``0/0``
      - ``0/0``
      - ``0/0/0``
      - ``0/1``
    * - ``0``
      - ``0/1``
      - ``1/0``
      - ``0/0``
      - ``0/0``
      - ``0/0``
      - ``0/0/0``
      - ``0/0``




But the operand means we need to do some series of steps
    use LDAR again

A look up table would be good, except we need several steps

So, let's make a new counter

    Show table example


SHOW IMAGE

Notice that table still follows binary count!


A matter of compleeting the table for every instruction



Look Up Table to Process Instruction
====================================



Including the Control Logic Module in the System
================================================



For Next Time
=============

* Something?


