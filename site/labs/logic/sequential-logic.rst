****************
Sequential Logic
****************

* Feel free to use your laptop
* You are strongly encourage to work with others

    * When you get stuck, ask those sitting around you for help
    * Get used to working together in the labs
    * Peer teaching and peer learning has been empirically shown to be very effective


For these questions, feel free to use a single Digital workspace for all the circuits. However, label each circuit with
labelled rectangles. These are components that can be found under "Components -> Misc. -> Decoration -> Rectangle".

Where possible, each question should have complete tests. The test component can be found under "Components -> Misc. ->
Test case". Once a test component is placed on the workspace, righ`t click on the component to edit the test data.

Questions may have restrictions on the logic gates that may be used. When restrictions are stated, they only apply to
the gates; inputs, outputs, wires, etc. may be still be used.



Latches & Flip-Flops
====================

#. Create a S-R Latch

    * Play with the circuit enough to become comfortable with all possible states and inputs
    * Do not forget to include tests for all circuits


#. Create a D latch

    * Simplify the circuit by eliminating the :math:`\lnot Q` output
    * Play with the circuit enough to become comfortable with all possible states and inputs


#. Create a D latch with Enable

    * Add a "Data Graph" component to the design

        * Can be found under "Components -> IO -> Data Graph"


    * Play with the circuit enough to become comfortable with all possible states and inputs


#. Create a D flip-flop

    * Add a new output component between the output of the first D latch and the second

        * Be sure to label this component


    * Read the Test component's help to learn how to handle the clock input

        * Right click the test component -> Edit -> Help


    * Be sure to include the new labelled output component to the tests
