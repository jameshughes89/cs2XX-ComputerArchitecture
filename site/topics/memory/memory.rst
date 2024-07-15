******
Memory
******

* Storing data for later use is an important function of a typical digital computer
* Memory can be used to store

    * Data, such as the value of a variable
    * Instructions, such as a program



Bits and Bytes
==============



Random Access Memory (RAN)
==========================

* Memory provides a way to store data for later use
* There are several different broad types of memory within a computer, but they all serve the same general purpose
* In this course, the types of memory that will be covered is

    * Random Access Memory (RAM) --- Stores data and instructions the computer is using
    * Registers --- Stores data and instructions the CPU is actively using


* For this topic, RAM will be the focus


Address Space and Addressability
--------------------------------

* In a typical computer, RAM stores data the computer is using along with the instructions of the programs being run
* RAM is commonly made up of a large number of memory *locations*
* Each of these memory locations stores some data/instruction
* Each memory location can be uniquely identified with a *memory address*
*




Address is the specific identifier of a location where data is stored
Addressability is the amount of information at each location


.. figure:: memory_abstract_idea.png
    :width: 500 px
    :align: center

    High-level visualization of RAM as a table. The left column contains each memory location's unique memory address,
    while the right column represents the data stored at the specific memory address. Here, the memory addresses are
    binary numbers and the data are represented as characters. The use of characters ``a`` through ``p`` in this figures
    is arbitrary and not meaningful.


* The above figure provides a high-level visualization of RAM
* In this figure, there are a total of 16 unique memory locations



* Each memory location contains some data, which is represented here as some character


warning though, can be confusing as both are bits

1GB meaning
    ability to address 1,000,000,000 unique bytes
    really, it's 1,073,741,824 though, as it's multiples of 2
    Metric prefixes are used for ease
    Sometimes MiB/GiB
    Explain why (think of address space)





256 Byte Memory Example
=======================



For Next Time
=============

* `Watch Ben Eater's video on S-R Latches <https://www.youtube.com/watch?v=KM0DdEaY5sY>`_
* `Watch Ben Eater's video on D Latches <https://www.youtube.com/watch?v=peCh_859q7Q>`_
* `Watch Ben Eater's video on D Flip-Flops <https://www.youtube.com/watch?v=YW-_GkUguMM>`_
* Read Chapter 3 Sections 4 of your text

    * 3 pages