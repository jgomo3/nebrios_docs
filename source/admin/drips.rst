Drips
=====

Drips are a way to schedule KVP input into your system. Just like any API or human (through the debug mode) can enter a KVP into the system, a Drip will do that on schedule.  You create drip by entering the schedule in cron sytax, and the KVP's you want to inject on that schedule. Drips always create a new PID when they are triggered. They are meant for introducing a new value to the system so that the scripts already present can react to them. 

.. image:: /img/drip.png

This window uses the same syntax as the debug window for adding KVPS

:: 

  key := value
  
  # to kick of a meeting process
  meeting := initiate
  
  # check the thermostat
  nest_temp_chec := true
  
  # check Google Drive for a new spreadsheet
  gdrive_search := xls
  
  # multiple lines work too
  gdrive_search := xls
  gdrive_search := doc
  gdrive_search := jpg
  
Here some cron examples to get you started also:

::
  
  # hourly
  0 * * * *
  
  # daily
  0 0 * * *
  
  # weekly
  0 0 * * 0
  
  # monthly
  0 0 1 * *
  
  # specific day - Jan 3
  0 0 03 01 *

Related is the :doc:`../builtins/schedule` keyword. Shedules are defined in scripts rather than the admin. They allow you to define a time when the script will wake up and try to run against every PID in the system. Drips on the other hand simply input a KVP on a schedule and the system takes if from there. Related, but very different.


