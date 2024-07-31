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

* Tri-state logic was discussed in the previous topic when introducing drivers

    * Drivers were used to control RAM out


* Briefly, components can have three different states

    * Output a high signal by connecting the line to some voltage source (``1``)
    * Output a low signal by connecting the line to ground (``0``)
    * High impedance state/do nothing (``Z``)


* Outputting ``0`` is not the same as outputting nothing since any other signal on the same line would be sunk to ground
* In other words, if two components are connected to the same output line

    * If one component outputs ``0`` by connecting the line to ground
    * And the other outputs ``1`` by connecting the line to a voltage source
    * The line would ultimately have no voltage as it would be connected to ground



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