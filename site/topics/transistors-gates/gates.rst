***********
Logic Gates
***********

* With clever configurations of transistors, boolean logic operators can be implemented
* This allows for the ability to perform logical operators on electrical signals

.. warning::

    More complex transistor configurations for each of the below logic gates are contained within the textbook. The
    reason for their added complexity is a consequence of the physical limitations of how transistors work. These
    more complex configurations would be more inline with how logic gates are actually physically built.

    Fortunately, the simulator being used for this course is idealized and several physical limitations are ignored,
    which allows for the simpler configurations to be used. Nothing will be lost by using the simpler configurations
    since (a) the abstract ideas are the same between the simple and complex configurations, (b) the more complex
    configurations are only necessary because of the physical properties of semiconductors, and (c) for the most part,
    transistors will not be directly interacted with going forward in this course.



And Gate
========

* Consider the **and** operator --- output ``1`` when both operands are ``1``, otherwise output ``0``

.. list-table:: Truth Table for **and**
    :widths: auto
    :align: center
    :header-rows: 1

    * - :math:`a`
      - :math:`b`
      -
      - :math:`a \land b`
    * - ``0``
      - ``0``
      -
      - ``0``
    * - ``0``
      - ``1``
      -
      - ``0``
    * - ``1``
      - ``0``
      -
      - ``0``
    * - ``1``
      - ``1``
      -
      - ``1``


* Knowing how transistors work as switches, how can two switches be configured to output ``1`` when they are both "on"?

    * When two input signals are ``1``, output ``1``, otherwise output ``0``


.. figure:: and_gate_with_transistors.png
    :width: 500 px
    :align: center

    Two transistors in series. Both transistors would need to be "on" in order for the signal at the top transistor's
    source (``1``) to reach the output at the bottom transistor's drain.


* With two transistors in *series*, both would need to be "on" for the signal to travel through to the output

    * *Series* meaning, one after the other along the same conductor
    * In a series circuit, the signal can only travel along the single conductor


* If either switch (or both) is "off", the signal could not travel to the output
* This perfectly corresponds to the **and** boolean operator
* This circuit is called an *and gate*

.. note::

    Each circuit seen so far has had a "Test" component. This allows one to create unit tests for circuits to help
    ensure correctness. Although the unit tests can get more complex and expressive, a simple form of unit tests for
    Digital is truth tables. Below is a unit test for the **and** circuit, which is the truth table defining how the
    circuit should behave.

    .. figure:: and_gate_unit_test.png
        :width: 666 px
        :align: center

        Unit test for the **and** circuit. Each column corresponds to a labelled input/output and each row specifies
        expected states.


* Boolean operators are used extensively within computer architecture
* Thus, special symbols are used to designate specific operators' gates
* Below is two images with the symbol for an and gate

    * The first image is of the symbol for the and gate
    * The second shows how the inputs and output would correspond to the full and gate built with transistors


.. figure:: and_gate_symbol.png
    :width: 500 px
    :align: center

    Symbol for an and gate.

.. figure:: and_gate_symbol_with_labels.png
    :width: 500 px
    :align: center

    Symbol for an and gate with labelled inputs and output corresponding to the *and gate* built with transistors.


.. note::

    This is the first major layer of abstraction that will be seen throughout this course. Instead of thinking of
    logic gates in terms of the whole schematic with transistors, they are represented as a single symbol.



Or Gate
=======

* For **or**, a signal of ``1`` should reach the output if either switch is "on"

.. list-table:: Truth Table for **or**
    :widths: auto
    :align: center
    :header-rows: 1

    * - :math:`a`
      - :math:`b`
      -
      - :math:`a \lor b`
    * - ``0``
      - ``0``
      -
      - ``0``
    * - ``0``
      - ``1``
      -
      - ``1``
    * - ``1``
      - ``0``
      -
      - ``1``
    * - ``1``
      - ``1``
      -
      - ``1``


.. figure:: or_gate_with_transistors.png
    :width: 500 px
    :align: center

    Two transistors in parallel. Either transistors would need to be "on" in order for the signal to reach the output.


* With two transistors in *parallel*, either would need to be "on" for the signal to travel through to the output

    * *Parallel* meaning, transistors on separate conductors that split from the same conductor and re-join
    * The parallel circuits, the signal can travel through each separate conductor


* Below is an image of the symbol for an or gate

.. figure:: or_gate_symbol.png
    :width: 500 px
    :align: center

    Symbol for an or gate.


Not Gate
========

* Now consider the **not** operator

.. list-table:: Truth Table for **not**
    :widths: auto
    :align: center
    :header-rows: 1

    * - :math:`a`
      -
      - :math:`\lnot a`
    * - ``0``
      -
      - ``1``
    * - ``1``
      -
      - ``0``



* The not gate is a little different from the and/or gates


.. figure:: not_gate_with_transistors.png
    :width: 500 px
    :align: center

    Not gate with a transistor. When the transistor is turned "on", the circuit's voltage will drop to neutral as ground
    would be directly connected to the output.


* Notice how the output is on the source end of the transistor
* This is because the output should be ``1`` when the gate is "off",
* But as soon as the gate is "on", the output should become ``0``

* If it is unclear how this works, consider that

    * When the transistor is "off", the signal from the voltage source, through the resistor, is connected to the output
    * When the transistor is "on", the output would be directly connected to ground, sinking the signal


* If still unclear, consider a plugged sink with a faucet running that is overflowing with water
* If someone removes the plug from the drain, the water can then flow through the drain and stop overflowing

    * This would be like what happens when the transistor is turned "on"


.. admonition:: Activity

    How would one configure the schematic for **not** if using a P-channel MOSFET instead of a N-channel like above?




* Below is an image of the symbol for a not gate

.. figure:: not_gate_symbol.png
    :width: 500 px
    :align: center

    Symbol for a not gate.


* However, not is sometimes represented as only the circle

    * In fact, the triangle in the gate means a *buffer* component


* It is also common to simplify a not input to another gate by adding a circle to the symbol's respective input
* Below is an example of an and gate with one input inverted

    * The top image shows one input explicitly inverted with a not gate
    * The bottom image is simplified to show that the input is inverted


.. figure:: not_added_to_and_gate.png
    :width: 500 px
    :align: center

    Two representations of an and gate with the top input being inverted.



Other Gate Symbols
==================

* Adding a circle to the output would signify an inverted output, like the below nor and nand gate symbols

.. figure:: nor_gate_symbol.png
    :width: 500 px
    :align: center

    Symbol for a nor gate.

.. figure:: nand_gate_symbol.png
    :width: 500 px
    :align: center

    Symbol for a nand gate.


* Another common symbol is for exclusive or (xor)

.. figure:: xor_gate_symbol.png
    :width: 500 px
    :align: center

    Symbol for a xor gate.


For Next Time
=============

* Check out the :download:`boolean operators built with transistors <boolean_operators_with_transistors.dig>` schematic for Digital
* Read Chapter 3 Section 3 of your text

    * 5 pages