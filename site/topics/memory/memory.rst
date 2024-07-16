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
* In this course, the types of memory that will be covered are

    * Random Access Memory (RAM) --- Stores data and instructions the computer is using
    * Registers --- Stores data and instructions the CPU is actively using


* For this topic, RAM will be the focus


Address Space and Addressability
--------------------------------

* In a typical computer, RAM stores data the computer is using along with the instructions of the programs being run
* RAM is commonly made up of some number of memory *locations*
* Each of these locations can be uniquely identified with a *memory address*
* The total number of uniquely identifiable locations is referred to as the *address space*

* Each of these memory locations stores some data or instruction
* The amount of data stored in each location is the memory's *addressability*
* Usually, RAM is *byte addressable*, meaning each memory location can store 1 byte/8 bits of data

.. figure:: memory_abstract_idea.png
    :width: 500 px
    :align: center

    High-level visualization of RAM as a table. The left column contains each memory location's unique memory address,
    while the right column represents the data stored at the specific memory address. Here, the memory addresses are
    four bit binary numbers and the data are represented as characters. The use of characters ``a`` through ``p`` in
    this figures is arbitrary and not meaningful.


* The above figure provides a high-level visualization of RAM
* In this figure, there are 16 unique memory locations, each identifiable with a four bit binary number
* Each memory address contains some data, represented here as some character

* If one, for example, asked what is stored at memory address 3 (``0011``), the answer would be ``d``
* However, like the memory address, the data being stored is some pattern of ``0``\s and ``1``\s



256 Byte Memory Example
=======================



For Next Time
=============

* `Watch Ben Eater's video on S-R Latches <https://www.youtube.com/watch?v=KM0DdEaY5sY>`_
* `Watch Ben Eater's video on D Latches <https://www.youtube.com/watch?v=peCh_859q7Q>`_
* `Watch Ben Eater's video on D Flip-Flops <https://www.youtube.com/watch?v=YW-_GkUguMM>`_
* Read Chapter 3 Sections 4 of your text

    * 3 pages