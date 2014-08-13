required
========

.. note:: This feature has been is being depreciated. We are moving towards pre-save KVP actions more like DBC on a class or function.

If you don't want a script to trigger from imporporly filled out KVP's use required. This is useful when your workflow needs values turned in at the same time. Maybe you don't want a first name without a last name. Rather than creating an additional script to catch theses mis-directions, just use required:

::

    required = [('first', 'last')]

A message will be sent to the user if they have submitted the values that break the required rule. If the interaction is via email, it will come as an email. Otherwise it will be returned as a message in the Nebri interactive mode.

