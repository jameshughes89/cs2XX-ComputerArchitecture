*******
The Bus
*******

* The bus physically connects several components within a computer
* It facilitates the transfer of information between these components, such as RAM and registers

* Typically, there are three types of busses

    * Data bus --- Transfer data between components
    * Address bus --- Transmits memory addresses
    * Control bus --- Sends signals responsible for controlling when components are active


* Depending on the system architecture, these busses can be physically separate or combined



Tri-State Logic
===============

Already discussed with drivers
on/off/high-impedance (z), meaning nothing

When 1, signal line is connected to a voltage source
When 0, it's not nothing, it's connected to ground
If a line is connected to ground and another component connects to voltage source, it will get sunk to ground
This is why Z is important, it's nothing


Analogy
Consider a long sink as a signal line like the ones on a bus

IMAGE

The line has several components connected to it, represented by the faucet and drain
When on, a tap is turned on and the sink fills
When off, a drain is opened, and anything left in the sink drains
Z state would be to do nothing --- no tap or drain

If one tap is on, but some other component has the drain open, then the water will drain, which is bad



Connecting Components
=====================



Loading Data into RAM
=====================



Swapping Data
=============



For Next Time
=============

* Read Chapter 2 Section 2 of your text

    * 2 pages