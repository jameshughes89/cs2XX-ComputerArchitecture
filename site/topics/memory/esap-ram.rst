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

As already already discussed

Memory address
address space
Each location in memory stores some amount of data --- addressability

The number of memory locations does not impact how many bits can be stored in each address
But, the number of addresses and addressabiity determins the amount of data stored

.. figure:: memory_abstract_idea.png
    :width: 400 px
    :align: center

    Visualization of RAM. The left column is memory addresses, and the right is the data stored at the respective memory
    address.


above example, 16 memory locations
    0000 -- 1111
    or can think 0 -- F

This needs 4 address lines to index ecah location

The amount of data in the above example is not clear, but the data data itself is represented by the 16 letters


We have a shared data and address bus
Although we have an 8 bit bus,
Due to the limitations of the system, we will only have 4 address lines
    will be clear later

16 possible addresses

4 bits can be moved on the bus to address RAM
each memory location will store 8 bits of data, that can be moved around by the bus


NOTE ON 32 bit comps?








Address Register
----------------



Including RAM in the System
===========================



Executing Arithmetic on the ALU with RAM
========================================



For Next Time
=============

* Something?

