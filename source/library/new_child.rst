new_child
=========

Any process can spawn a new process with the new_child call. That means if you are in PID 1, and create a child process, it will be PID 2, assuming that's the next available PID available. 

In order to do this you must call new_child and give it a kvp. Instead of using *self.example_kvp* you would use:

::
    
    new_child.example_kvp

This would create *example_kvp* with a PID of 2. That KVP is fully stand alone, fully KVP.  The difference is that the PID 2 (in this example) stores information about who its parent is. 

.. note:: new_child is used inside of action() generally

    You only create new_children from a script that is already woken up because it was scheduled to, or a KVP it was listening to was updated. That's the Nebri way to get anything done!

You can put any amount of new_children calls in a script. All those children KVP's spawn under the same PID. For instance:

::
    
    new_child.example_kvp
    new_child.foo
    new_child.bar

... will all spawn under the same PID. Same with this:


::
    
    new_child.example_kvp

    def some_function()
        pass

    new_child.foo

    # MOAR_CODE_HERE!!!

    new_child.bar

If you want to create new KVP's under multiple new PID's, the script that is calling new_child must be woken up for each new PID you want to create.


Listening To New Children
*************************

You created example_kvp and now want to know when it changes. You can listen to it like this:

::

    listens_to = ["child.example_kvp"]

See, normally you can't have one PID interacte with another PID's KVP's. However it's possible with the Parent/Child relationship now. Another way to share information across PID's is to use :doc:`shared_kvp`. 
