Debug Mode
~~~~~~~~~~

This view is only available to admins within the system. It's a tremendous help when authoring scripts. When the system executes anything in association with your email address, you will get to see what script was triggered, what triggered it, what changed before and during the script execution, and much more. Within a few minutes you can write a script and fully test it.

.. image:: /img/nebri_debug.jpg

The Email window basically spoofs an email client. You can quickly send in KVPs like 

:: 

  foo := bar
  
Or to send in a dictionairy:

::

  smart_message := '{"priority": 3, "to": "adam", "message": "Site is down! Get it going ASAP!"}'

It's the same syntax when writing emails. The system console will then show, realtime, what the system is doing in reaction to your changes.

Even when you are working with forms it's great to keep the debug window open. It will tell you when a script fired, if the check() passed or not, what KVP's got modified as a result, and other things.


