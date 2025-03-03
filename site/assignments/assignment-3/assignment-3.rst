************
Assignment 3
************

* **Worth**: 5%
* **DUE**: Monday March 17, 11:55pm; submitted on MOODLE.



Provided Files
==============

Incomplete Digital files are provided for the questions. These files contain tests, a resizable designated space for
building circuits, and labelled inputs, outputs, and other components.

:download:`These files can be downloaded from here. <assignment_3-dig_files.zip>`

Uncompress this folder and open the files within Digital. Each question specifies which of the file to work in.



Part 1 --- Registers
====================

#. Create a circuit to swap data between several registers

    * Data can be moved between 8 different sources/destinations

        * Seven 8 bit registers
        * The circuit will also have the ability to read/write from data in/out

            * The source may be data in, or the destination may be data out


    * This circuit will have one 8 bit output serving as data out
    * This circuit will have a total of 8 inputs

        * A clock input
        * One 8 bit input serving as the data in
        * Three bits specifying the source

            * Registers 0 -- 6 are referred to by their corresponding bit patterns

                * For example, ``011`` refers to register 3


            * Data in is referred to by the bit pattern ``111``


        * Three bits specifying the destination

            * Registers 0 -- 6 are referred to by their corresponding bit patterns
            * Data out is referred to by the bit pattern ``111``


    * For example, consider the following source and destination bit patterns

        * ``111`` ``000`` --- move the contents from data in into register 0
        * ``000`` ``001`` --- move the contents from register 0 into register 1
        * ``001`` ``111`` --- move the contents from register 1 to data out






Some Hints
==========

* Work on one part at a time
* Some parts of the assignment build on the previous, so get each part working before you go on to the next one
* Test each design as you build it

    * This is a really nice thing about these circuits; you can run your design and see what happens
    * Mentally test before you even implement --- what does this design do? What problem is it solving?


* If you need help, ask

    * Drop by office hours



Some Marking Details
====================

.. warning::

    Just because your design produces the correct output and the tests pass, that does not necessarily mean that you
    will get perfect, or even that your design is correct.


Below is a list of both *quantitative* and *qualitative* things we will look for:

* Correctness?
* Did you follow instructions?
* Label names?
* Design, layout, and style?
* Did you do weird things that make no sense?



What to Submit to Moodle
========================

* Submit your completed Digital (*.dig*) files to Moodle
* Do **not** compress the files before uploading to Moodle


.. warning::

    Verify that your submission to Moodle worked. If you submit incorrectly, you will get a 0.



Assignment FAQ
==============

* :doc:`See the general FAQ </assignments/faq>`
