=============================
Conditional Jump Instructions
=============================

* The various status flag values can now be determined and stored in the flags register
* However, how should the conditional jumps be handled by the control logic?
* Further, the existing control logic needs to be updated to now handle the new flag register control signal

    * When should the system's status signal values be stored stored in the flags register?



Conditional Jump Control Logic
==============================



Including the Flag Register in the System
=========================================

Physically, Hook it up

Connect the ALU output to the input of the status flag logic
replace the old LUT design with the new

    * 3 new inputs
    * 1 new output controlling the flag reg enable

connect the signal from the LUT to the status flag enable

IMAGE OF WHOLE SYSTEM


Still need to update the control logic
new script for this
SHOW CODE EXAMPLES



Programming with Conditional Jumps
==================================



For Next Time
=============

* Something?


