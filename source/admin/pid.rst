PID
~~~

PID stands for ''Process Identifier'' or ''Process ID''. This is simply the ID given to a group of KVP's. Every KVP has a PID in fact. You see, before a KVP is registered into Nebri it **must have a PID**. If Nebri isn't told which PID the KVP belongs to, it **generates a new PID** and then inputs it. 

Image you have a KVP with ''release := 10/2/2017'' that gets spit into Nebri from your chatbot. If it isn't in response to any other KVP or script (in this case it's not), it creates a new PID. 

.. note:: Creating many thousands of PID's isn't an issue until you use a :doc:`schedule`. Even then we are adding filtering mechanism for a future release to improve this.

If our ''release'' KVP actually had a PID associated, we would have made sure to send it along. In this case our chatbot would have sent the PID along to on of your :doc:`api` endpoints as a keyword argument along with the KVP. ''And this is where the power comes in!'' This mechanism of creating a PID or resuming the work a PID already started gives you the ability to track unlimited releases! Any other process for that matter. See, one release might have started a month ago, and another would have started today. Each release "process" would have carried it's own PID, and thus carry it's own history.  You still have the ability to operate from an old release if you like. That would come in handy if you needed to track which step took the longest, or even finish up one that never fully completed.

