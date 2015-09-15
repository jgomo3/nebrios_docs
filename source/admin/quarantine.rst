Quarantine
~~~~~~~~~~

This is a place where all your sick scripts go. If ever a script is triggered and unable to completely run because of an error or timeout, you will fine it listed in the quarantine. There you will see the script name and time of error, along with the error message that was generated.

It gets better! For errors, once the script is updated in any way (probably in hopes of fixing the error), it's triggered again to try and run and the old quarantine is deleted. Should the script happen to error again it will create a new quarantine. Otherwise, you are good to go.

For time-outs, the script is disabled when the quarantine is created. This way you instance will not break because of one hung script. If you want be made aware of a paused script, you have notification options. 

Notificaiton
============
Whenever a quarantine is generated, after the KVP Bag for the Process in question has been rolled back, two KVPs are added to the Process: 

  * quarantined_script (has the name of the script that failed)
  * quarantine_error (contains the exception or error as a string)
  
All you need at this point is a script to watch for one of these KVP's and contact the appropriate person for repairs. Often adding proper try/except architecture will keep timeouts and errors from creating quarantines. 

Another monitoring option is to check from a script woken up by a drip with a :doc:`../builtins/process_ORM` query: this is better for many situations where timeouts or other errors leave the system in an uncertain state. Our monitoring will now restart instances after timeouts, but this means that the wakeups may be lost, and so the Process ORM query from a drip becomes necessary.



