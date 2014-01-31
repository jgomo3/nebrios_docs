******
parent
******

This built-in allows a child to connect to it's parents KVPs, should it have any.

::

    listens_to = ["parent.example_kvp"]


If the PID you are calling from doesn't have a parent, the listen_to will never trigger. See :doc:`../scripts/parent_child`.
