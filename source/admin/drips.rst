Drips
=====

Drips are a way to schedule KVP input into your system.  You create a cron and KVP values you want to be entered on that schedule. Drips always create a new PID when they are triggered. They are meant for introducing a new value to the system so that the scripts already present can react to them. An example might be a meeting reminder. A drip might be set for every Tuesday that creates this KVP: 

:: 

  meeting_today := True. 

It will create a new PID, and your meeting reminders can be sent out, or pre-meeting questionair can be filled out.

The KVP input format is the same as used in emails and the debugger. 

Related is the :doc:`../builtins/schedule` keyword. Shedules are defined in scripts rather than the admin. They allow you to define a time when the script will wake up and try to run against every PID in the system. Drips on the other hand simply input a KVP on a schedule and the system takes if from there. Related, but very different.


