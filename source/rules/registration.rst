************
Registration
************

The following parts should be found at the top of your script, and they comprise the "registration" of the script.

Listening
=========

Since Nebri OS scripts don't ever execute by being called directly, you will need to specify what KVPs in the system, when created or changed, will trigger the script. This is done by using the listens\_to list. It can contain any number of KVPs to watch. Usually other scripts, forms, API's or incoming emails will change KVPs, and thus trigger your script.

This is the listens\_to list.

.. code-block:: python

    class my_class_name(NebriOS):
        listens_to == ['some_value']
                    

"some\_value" is the KVP that you are telling your system to react to. As an example, let's say we want to watch vacation\_request KVP. That way, if anyone sent in an email to your Nebri OS Inbox with something like "vacation\_request := True", the script would wake up, and try to move on.

Listening to multiple KVPs looks like this:

.. code-block:: python

    listens_to == ['some_value', 'foo', 'bar']
                  

If any one of those KVPs were to change, the script would wake up.

.. note:: You can listen to every single KVP using the wild card: listens_to == ['\*'] 

Schedule
========

An extremely useful alternative to listens_to is :doc:`../builtins/schedule`. You can define when the script wakes up and acts rather than what it listens to. This is useful in a monitoring situation. For example, every night you want to make sure doors are shut, or nothing is overdue.  

