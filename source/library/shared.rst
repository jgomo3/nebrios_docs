************
Shared KVP's
************

Want to create a KVP that is globally accessible to any PID? Here's how to create a shared KVP:

::

    shared.example_kvp == "foo" 

Instead of using *self*, you use *shared*.

Since shared data isn't necessarily initiated from the PID you are standing in, it's important to check that it exists before changing it:

:: 

        if shared.idle_dev_number:
            shared.idle_dev_number -= 1

Also you can treat it differently if it doesn't exist:

:: 

        if shared.idle_dev_number:
            shared.idle_dev_number -= 1
        else:
            shared.idle_dev_number = 0

