=============================
Conditional Jump Instructions
=============================

* The various status flag values can now be determined and stored in the flags register
* However, how should the conditional jumps be handled by the control logic?
* Further, the existing control logic needs to be updated to now handle the new flag register control signal

    * When should the system's status signal values be stored stored in the flags register?



Conditional Jump Control Logic
==============================

clear up what they are
jump when the respective status flag is high, otherwise, ignore and carry on
    for example...

So, what should that logic look like?
turns out, the logic already mostly exists, it's the jump

    SHOW LOGIC?

BUT, we still need a way to ignore

    SHOW LOGIC (NOOP)
    It's a NOOP


How can it know?
Use the same idea as the signed control signal
    when the flag is off, do NOOP
    when the flag is on, do jump


Discussed in more details below, but it really is the same idea as the output register
    could have a multiplexer and multiple LUTs
    or we could have additional inputs to the LUT specifying chunks of the LUT for the various cases
    this means we will have 8x the size of the LUT though


Ok, so we also need to control the status flags



Including the Flag Register in the System
=========================================



Programming with Conditional Jumps
==================================



For Next Time
=============

* Something?


