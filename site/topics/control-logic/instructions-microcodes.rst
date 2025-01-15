===========================
Instructions and Microcodes
===========================

* Although RAM has currently only held data, computation has been performed on the system
* With careful manipulation of the control signals, specific operations were executed by the system

    * Reading and writing to RAM
    * Performing arithmetic
    * Outputting values
    * Looping


* Realizing this, it becomes possible to create a set of well defined instructions for the system



Constraints
===========



Microcodes
==========

* In several previous topics, it was observed that operations were performed by moving data around the system

    * Moving data around to different modules
    * Some modules output data, while others input


* Consider the operation of loading data from some memory address into register A

    * Any of the 16 memory addresses could be used in this example, but ``15`` (``0b1111``) is used here


* Think about the steps involved to perform this operation within the context of the ESAP system design

    #. Load the value of the target memory address (``0b1111``) from the bus into the memory address register
    #. Output the value stored in RAM to the bus and input the value from the bus into register A



IMAGE

what are the steps?
    - spell out

have table?

IMAGES

in fact, consider the operation being ``XXXX 1111`` where ``1111`` is the address and ``XXXX`` the unique identifier for the operation LOAD A

These small steps are put together to achieve the operation/instruction of loading data from RAM into A
These are called micro codes

Most of our instructions are made up of several micro codes
what they are are up to the designer
how many there are depends
Thus, we cna see why 1 instruction takes several clock cycles



Fetch and Instruction Register
==============================



Instruction Set
===============



For Next Time
=============

* Something?


