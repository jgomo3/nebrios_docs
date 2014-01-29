Debug Mode
~~~~~~~~~~

This view is only available to admins within the system. It's a tremendous help when authoring scripts. When the system has executes anything in association with your email address, you will get to see what script was triggered, what triggered it, what changed before and during the script execution, and much more. Within a few minutes you can write a script and fully test it.

The Email window basically spoofs an email client. You can quickly send in KVPs like foo := bar. It's the same syntax when writing emails. The system console will then show, realtime, what the system is doing in reaction to your changes.

Even when you are working with forms it's great to keep the debug window open. It will tell you when a script fired, if the check() passed or not, what KVP's got modified as a result, and other things.

Access Control List (ACL)

This is where you can define who can access which KVPs on your system. When a user is disallowed from viewing a KVP, it will not show up in any email or communication to them. Nor will they have access to modify it. An example of an ACL setting is to protect employees from seeing the pay\_rate of a new hire.

.. figure:: /img/nebri_acl.jpg
   :align: center
   :alt: 

