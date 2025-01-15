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

as we have seen, performing operations is a process of moving data around different modules

Consdier loading data from some memory address, say 15, and putting it into register A
consider in the context of our system
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
Thus, we cna see why 1 instruction takes several clock cycles



Fetch and Instruction Register
==============================



Instruction Set
===============



For Next Time
=============

* Something?


