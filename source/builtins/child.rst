*****
child
*****

This built-in allows you to interact with children KVP's that you have spawned from a parent PID. Assuming you are standing in a PID that has children KVP's, this is how you can listen for changes: 

.. code-block:: python

    listens_to = ["child.example_kvp"]

If the PID you are calling from doesn't have a child, the listen_to will never trigger. See :doc:`../rules/parent_child`.

This next part gets a little tricky. Since a parent can have multiple children with the same KVP key, like example_kvp, you can't reference the KVP's exactly the same as regular KVPs. There are two ways to go about modifying children KVPs. 

First, you can listen to a child KVP. This allows you to modify the KVP inside of that parent script. To put it another way, you can't modify a child KVP without listening to it without a special work around. For example, this will not work:


.. code-block:: python

    class example(NebriOS):
        listens_to = ["child.example_kvp"]

        def check(self):
            ...

        action(self):
            child.another_kvp = "save this string!"


But this works:

.. code-block:: python

    class example(NebriOS):
        listens_to = ["child.example_kvp"]

        def check(self):
            ...

        action(self):
            child.example_kvp = "save this string!"



You can't modify *child.another_kvp* because the script can't know which child you are referencing. Multiple children can have *another_kvp*. You can however modify *child.example_kvp* because in this instance the script would have only come alive a specific PID was changing this KVP, thus providing a referencable context.

The second method we provide is simple way to loop through your children and identify the ones you want to modify and/or read.  This done using the :doc:`children` tool.



    
