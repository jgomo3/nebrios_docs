Listening
~~~~~~~~~

Since Nebri OS scripts don't ever execute by being called directly, you will need to specify what KVPs in the system, when created or changed, will trigger the script. This is done by using the listens\_to list. It can contain any number of KVPs to watch. Usually other scripts, forms, API's or incoming emails will change KVPs, and thus trigger your script.

This is the listens\_to list.

::

    class my_class_name(NebriOS):
        listens_to == ['some_value']
                    

"some\_value" is the KVP that you are telling your system to react to. As an example, let's say we want to watch vacation\_request KVP. That way, if anyone sent in an email to your Nebri OS Inbox with something like "vacation\_request := True", the script would wake up, and try to move on.

Listening to multiple KVPs looks like this:

::

    listens_to == ['some_value', 'foo', 'bar']
                  

If any one of those KVPs were to change, the script would wake up.

**Note:**\ You can listen to every single KVP system wide by using \* instead of a text value.

**Read more: `Writing Scripts - Registration </tutorial#registration>`_**



