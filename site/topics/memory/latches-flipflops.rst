**********************
Latches and Flip-Flops
**********************

* The combinational logic topic covered circuits that did not store or require any stored data to operate
* Here, circuits capable of storing data for later use will be covered
* These can later be used to construct more complex circuits that make decisions based on a series of possible states



Set-Reset Latch (S-R Latch)
===========================

* One of the most basic circuits for storing data is a set-reset latch (S-R latch)
* What's unusual about this circuit is that it has internal feedback

    * The output of the circuit is fed back into itself as input


.. figure:: transistors.png
    :width: 333 px
    :align: center

    An S-R latch using NOR gates. The :mathc:`S` means "set", :math:`R` is "reset", :math:`Q` is the bit being stored,
    and :math:`\lnot Q` is the inverse of the bit being stored. Notice how the outputs of the circuit (:math:`Q` and
    :math:`\lnot Q`) also serve as two of the four inputs to the circuit.


.. note::

    There are several possible designs for an S-R latch. The textbook uses a similar design to the above image, but
    instead uses two NANDs instead of NORs. Although this NAND based design would work slightly differently, the general
    idea is the same.






* Truth table

    * What the labels mean

* Quiet state, but unstable
* Set
* Reset
* Both on means nothing


S-R Latch with Enable
---------------------

* Sometimes we want to control when the latch is actually "enabled"
* Show image
* Show truth table?

* Oscillating state
* But really, there's no need to try to set and reset at the same time...



Data Latch (D Latch)
====================



D Flip-Flop
===========



For Next Time
=============

* Read Chapter 3 Section 6 of your text

    * 14 pages