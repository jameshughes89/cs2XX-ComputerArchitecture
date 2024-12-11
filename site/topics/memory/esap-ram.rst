************************
Address Register and RAM
************************

* RAM stores data and instructions for the computer
* The values in RAM are temporary

    * RAM is not designed for long term storage
    * It is designed to store values the computer is working with  


* Although RAM was discussed in earlier topics, it is time to incorporate it into the ESAP system design



RAM Module
==========

Address Register
----------------

* shared busses
* problem as data on bus on bus is always changing, but ram address may want to be fixed
    * in others words, EXAMPLE
        * Store a value other than 0 into address 0

* Thus, there needs to be a way to seperate the data bus and address
* Simple solution is to have a register to store the address
    * store address into register, which is persistent until updated
    * Now data on bus can change without messing up the RAM address
    *


SHOW IMAGE

* Really, there is a seperate address bus, which is what connects the address register and RAM

* as previously discussed, only 4 bits from the main data bus will be used for the address
* That's why we ignore the 4 bits via the splitter

* Talk about an example of what one could do here

    * Store a memory address into the address register




Including RAM in the System
===========================



Executing Arithmetic on the ALU with RAM
========================================



For Next Time
=============

* Something?

