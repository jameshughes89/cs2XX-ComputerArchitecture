****************
Comparing Values
****************

* Feel free to use your laptop
* You are strongly encourage to work with others

    * When you get stuck, ask those sitting around you for help
    * Get used to working together in the labs
    * Peer teaching and peer learning has been empirically shown to be very effective


For these questions, feel free to use a single Digital workspace for all the circuits. However, label each circuit with
labelled rectangles. These are components that can be found under **Components -> Misc. -> Decoration -> Rectangle**.

Where possible, each question should have complete tests. The test component can be found under
**Components -> Misc. -> Test case**. Once a test component is placed on the workspace, right click on the component to
edit the test data.

Questions may have restrictions on the logic gates that may be used. When restrictions are stated, they only apply to
the gates; inputs, outputs, wires, etc. may be still be used.



Conditions
==========

#. Create a circuit to check if a given 8 bit signed integer is zero

    * In other words, check if some value ``== 0``
    * This circuit must take 8 inputs representing the 8 bit signed integer
    * This circuit will have one output

        * Output ``0`` when the value does not equal zero
        * Output ``1`` when the value is zero


#. Create a circuit to check if a given 8 bit signed integer greater than zero

    * Check if some value ``> 0``


#. Create a circuit to check if a given 8 bit signed integer greater than or equal to zero

    * Check if some value ``>= 0``



Specifying Operators
====================

#. Create a circuit that can perform a specific comparison of an 8 bit signed integer based on some input pattern

    * This circuit must take 8 inputs representing the 8 bit signed integer
    * This circuit must also take 3 additional inputs specifying the comparison to perform

        * ``000`` --- Always output ``1``
        * ``001`` --- ``== 0``
        * ``010`` --- ``> 0``
        * ``011`` --- ``>= 0``
        * ``100`` --- Always output ``0``
        * ``101`` --- ``!= 0``
        * ``110`` --- ``<= 0``
        * ``111`` --- ``< 0``


    * **Hints:**

        * Pay special attention to the order of the operators with respect to their 3 bit pattern
        * Mind the affect of the most significant bit on the operators



Comparing Numbers
=================

Two numbers
