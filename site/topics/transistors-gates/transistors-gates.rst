***************************
Transistors and Logic Gates
***************************

* When talking about electricity and semiconductors, things can get rather nuanced and complex
* However, the level of detail covered for this topic will be kept appropriate for the course content
* As such, certain analogies and ideas will be used that are technically inaccurate, but sufficient for our needs



Symbols
=======

* For this course, software called `Digital <https://github.com/hneemann/Digital>`_ will be used to create digital circuits
* There are a number of symbols representing components that will need to be understood
* Although some of you may be familiar with electronic component symbols, there are some things to note

    * Certain components have different symbols depending on their context
    * Some components have different symbols in different regions of the world


* When using Digital

    * An up arrow is used to signify a positive charge
    * A single horizontal line represents ground --- something with no charge; neutral
    * Typically, within the context of computer architecture, the voltage between this positive charge and ground is 5V


.. figure:: vcc_ground.png
    :width: 50 px
    :align: center

    Screenshot from Digital of a positive charge (up arrow) connected directly to ground (horizontal line).


* A single horizontal line is common within computer architecture and is the symbol found in Digital

    * There are other common symbols for ground depending on the context of how it is used


.. figure:: ground_symbols.png
    :width: 333 px
    :align: center
    :target: https://en.wikipedia.org/wiki/Ground_(electricity)

    Examples of three commonly used ground symbols. These have slightly different meanings, but all ultimately signify
    something with a neutral charge.


* In the above example, a voltage source was connected directly to ground
* In practice, this is a bad idea as that could cause damage and injury

    * Current would be too high


* A resistor, for example, could be added to the circuit to limit its current
* Below is an example of the simple circuit containing a resistor

.. figure:: vcc_resistor_ground.png
    :width: 50 px
    :align: center

    Screenshot from Digital of a positive charge (up arrow) connected to ground (horizontal line) through a resistor
    (box).


* In North America, a sawtooth symbol is used to represent a resistor, but elsewhere in the world it is typically a box

    * Like in the above figure


* Digital was not made in North America, thus, it makes use of the box symbol

.. figure:: resistor_symbols.png
    :width: 333 px
    :align: center

    Left --- Typical symbol for a resistor in North America. Right --- Typical symbol for a resistor outside North
    America.


* One of the commonly seen symbols for transistors are actually only for a specific, but common type of transistor

    * Bipolar Junction Transistors (BJT)


* The transistors available within the simulator Digital are Metal-Oxide-Semiconductor Field-Effect Transistors (MOSFET)

    * These transistors are common within computers


* The symbol used in this course for transistors will be of MOSFET transistors


.. figure:: transistor_symbols.png
    :width: 333 px
    :align: center

    Left --- Symbol for a Bipolar Junction Transistor (BJT). Right --- Symbol for a Metal-Oxide-Semiconductor
    Field-Effect Transistor (MOSFET).



Transistors
===========



Logic Gates
===========



For Next Time
=============

* Read Chapter 3 Section 3 of your text

    * 5 pages