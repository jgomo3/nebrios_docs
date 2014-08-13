Drips
=====

You might think of drips as a cron on your system, but much more simple. Drips **only** allow you to set a schedule for updating KVPs. That's it. They are meant for introducing a new variable to the system so that the scripts already present can handle the rest. An example might be a meeting reminder. A drip might be set for every Tuesday that creates the KVP meeting\_today := True. It will create a new PID for each drip.

Related is the :doc:`../builtins/schedule` keyword. Shedules are defined in scripts. They allow you to define a time when the script will wake up and try to run against every PID in the system. Related, but very different.


