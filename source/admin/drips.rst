Drips
=====

You might think of drips as a cron on your system, but much more simple. Drips **only** allow you to set a schedule for updating KVPs. That's it. They are meant for introducing a new variable to the system so that the scripts already present can handle the rest. An example might be a meeting reminder. A drip might be set for every Tuesday that creates the KVP 

:: 

  meeting_today := True. 

It will create a new PID for each drip. The KVP input format is the same as used in emails and the debugger. 

Related is the :doc:`../builtins/schedule` keyword. Shedules are defined in scripts rather than the admin. They allow you to define a time when the script will wake up and try to run against every PID in the system. Drips on the other hand simply input a KVP on a schedule and the system takes if from there. Related, but very different.


