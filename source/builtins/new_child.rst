new_child
=========

Any process can spawn a KVP under a new PID with the new_child call. That means if you are in PID 1, and create a child KPV, it will have a PID of 2, assuming that's the next available PID available. 

In order to do this you must call new_child and give it a kvp. Instead of using 

::

    self.example_kvp
    
you would use this:

::
    
    new_child.example_kvp = True

That KVP is full stand alone KVP. The only difference is that the new child KVP stores information about who its parent is. 


You can put any amount of new_child calls in a script. All those children KVPs spawn under the same PID. For instance:

::

    new_child.example_kvp = True
    new_child.foo = "fighters"
    new_child.bar = 225

.. note:: any amount of new_child calls in a single scripts creates KVP's under the same, new, PID. The PID doesn't increment for each new_child call. 

Listening To New Children
*************************

You created example_kvp and now want to know when it changes. You can listen to it like this:

::

    listens_to = ["child.example_kvp"]

See, normally you can't have one PID interacte with another. However it's possible with the Parent/Child relationship now. Another way to share information across PID's is to use :doc:`shared`. 

See :doc:`child`. 
