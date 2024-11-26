**********************************
Arithmetic logic Unit and the ESAP
**********************************

* The Arithmetic Logic Unit (ALU) is a combinational logic circuit for integer arithmetic and logical operations
* ALU designs can vary significantly and has implications for the total design of the computer



The Idea of the ALU
===================

.. figure:: alu_symbol.png
    :width: 500 px
    :align: center
    :target: https://en.wikipedia.org/wiki/Arithmetic_logic_unit

    Generic symbol for an ALU.


* With sophisticated ALUs, some operation is applied to the inputs (operands) to produce some output
* The operator is specified with some *opcode* passed to the ALU
* These operations may include

    * Addition/Subtraction
    * Increment/Decrement
    * AND/OR/XOR/NOT
    * Bit Shift/Rotate


* Further, the ALU may update the system's status flags, and, in turn, may behave differently depending on the flags

    * For example, the system may remember if the last operation resulted in an output of zero
    * Status flags are a topic to be discussed later


* Digital does not have a built in ALU like the other components discussed so far

    * However, it does have a custom ALU one can import
    * Although, this custom ALU will not be used here


.. figure:: alu_digital_symbol.png
    :width: 150 px
    :align: center

    Digital's importable ALU.


* Designing a sophisticated ALU is not difficult
* However, integrating one into a larger architecture may challenging
* Thus, to start, a simple ALU will be built and used
* Even with the simple ALU, the system being designed will be Turing Complete


.. note::

    One may have noticed that the ALU is effectively a function that takes inputs to produce outputs. However, one may
    also notice that this function may have *side effects* --- changing system status flags.

    In your computer science courses there has been a strong emphasis on avoiding side effects and writing pure
    functions, which this seems to violate. For better or worse, under the hood, the common modern designs/architectures
    for computers are very stateful and full of side effects.

    Fortunately, as one goes to higher levels of abstraction, like software, systems are designed such that side effects
    can be eliminated, despite the fact that the underlying hardware is stateful.



The Eater Simple as Possible Architecture (ESAP)
================================================

* The base architecture for the system being built is the *Simple as Possible* (SAP) design [#]_

    * Created by Malvino & Brown


* `There exist several versions of the SAP design <https://en.wikipedia.org/wiki/Simple-As-Possible_computer>`_
* For this course, a modified version of the SAP architecture by Ben Eater is used

    * This architecture will be referred to as Eater's SAP, or *ESAP*
    * `Ben Eater has a YouTube playlist of him physically building this computer on breadboards <https://www.youtube.com/playlist?list=PLowKtXNTBypGqImE405J2565dvjafglHU>`_
    * Note, however, that slight modifications to this design are made for the purposes of this course


.. figure:: esap_architecture_overview.png
    :width: 500 px
    :align: center
    :target: https://en.wikipedia.org/wiki/Simple-As-Possible_computer

    Overview of the ESAP Architecture. Arrows show how data is transferred between components of the computer system.
    With this design, the address and data bus are not entirely separate. This overview does not show the control bus.


* The design is simple to follow and understand, while still being Turing Complete

    * Further, it is straightforward to add to
    * It will also serve as the basis of going deeper in architecture complexity


* The ALU will serve as the starting point for building a computer with this architecture



Design of the ESAP ALU
======================

.. figure:: esap_alu.png
    :width: 500 px
    :align: center

    Configuration of the ESAP ALU connected to a data bus and control bus within Digital. This ALU always calculates the
    sum (or difference) of the integer values stored in registers A and B.


* The ESAP ALU is only capable of performing addition and subtraction

    * A control line (:math:`sub`) controls if the ALU performs addition or subtraction


* The ALU is always calculating the sum/difference of the two integer values stored in registers A and B

    * Loading from the data bus into the registers is controlled by :math:`A_{i}` and :math:`B_{i}`
    * There is control logic for the registers to output to the data bus (:math:`A_{o}` and :math:`B_{o}`)
    * There is no control for the registers' output to the adder
    * Thus, the adder always has the sum/difference of whatever data is stored in A and B


* Although the ALU is always calculating the sum/difference, its output is controlled with a control signal

    * :math:`ALU_{o}`


.. figure:: esap_alu_vs_architecture_overview.png
    :width: 666 px
    :align: center

    Comparison of the ALU and the ESAP architecture overview. This ALU includes several parts of the whole ESAP design
    --- two registers, ALU, clock, and data bus. The ALU does include the start of the control bus for the whole system
    (the vertical signal lines on the right hand side of the ALU), which is not shown in the architecture overview.


* It is possible to see how the ALU fits into the whole ESAP architecture design
* With the ALU, several components of the whole system are present

    * Register A
    * Register B
    * ALU
    * Data bus
    * Clock


* Further, the ALU does include the start of the control bus for the system

    * This is not shown in the ESAP architecture overview
    * A control bus will be required for the system to function


* One may have noticed the layout of register B and the ALU are swapped

    * ALU is below both registers in the Digital design, but between the registers in the overview
    * This difference is effectively irrelevant
    * As long as the inputs/outputs are configured correctly, this will have no functional impact on the system


* However, there is one slight difference that will have a functional impact on the system --- register B out

    * The designed ALU's register B can receive input from and output to the data bus
    * But the architecture overview shows that register B can only receive input


* Adding the ability to output from register B does provide some additional, yet minimal, flexibility to the design
* The original design does not allow for outputting from register B due to physical constraints and the minimal benefit

    * Remember, the original design was physically built on breadboards



For Next Time
=============

* Something?


----------------------

.. [#] Albert P. Malvino and Jerald A. Brown. *Digital computer electronics.* Glencoe/McGraw-Hill, 1992.