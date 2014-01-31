*****
child
*****

This built-in allows you to call children that you have spawned from a parent PID. 

::

    listens_to = ["child.example_kvp"]


If the PID you are calling from doesn't have a child, the listen_to will never trigger. See :doc:`../scripts/parent_child`.
