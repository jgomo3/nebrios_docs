***********
load_card()
***********

Allows a user to load a card into the interactive view. By calling:

::
    
    load_card(hello_world)
        # or any other card name 

...you will bring up the hello_world Polymer card, assuming you have one. The card will show for the user who activated the script, which then called load_card(). For example, you might have a welcome_message.py rule script which welcomes new users to your Nebri instance.  A new user would then be the last_actor which activated welcome_message.py, thus bringing up hello_world card. 

Parameters
==========

.. code-block:: python

    load_card(element_name)
        # required args

    load_card(element_name, pid, user)
        # all/optional args

    load_card(hello_world, pid=5023, user=sam@example.com)
        # example usage A

    load_card(hello_world)
        # example usage B 
