===============
Output Register
===============

* The look up tables provides a simple way to convert binary numbers to their seven segment display patterns
* Now, a register will be incorporated into the design to provide control over which data is being output to the display



Output Module
=============

* With the LUT and seven segment display configuration, it is possible to output values from our system
* However, like with the memory module, there needs to be a way to separate the data to be output from the bus

    * Otherwise, the display would show whatever is currently on the bus


* Thus, like with the memory module, a register will be used to store the value that is of interest
* This register will be called the *output register*
* The seven segment displays will always show the contents of the output register


IMAGE

with this design, we cna control when we load data into reg
no need to output data from reg

The signed signal reall yis treated like a control signal



Including Output in the System
==============================



Example of Outputting from the System
=====================================



For Next Time
=============

* Something?


