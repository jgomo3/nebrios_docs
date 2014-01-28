Executing
~~~~~~~~~

Anything under the action() function gets executed IF the script is woken up (based on what it listens\_to), AND the check() has returned as True. There is where emails are sent, logic is evaluated, APIs are called, other KVPs are set.

Send an email to anybody

Changing a KVP

Example gtalk plugin

::

    def action(self):
        send_email("email", """message""")
        self.vacation_status == "Finished"
        gtalk.send("recipient", """message""")
                  

Once you have a listens\_to, check() and an action(), you have the general body of a script.
 Check out the `Demo <demo>`_ for some script examples!


:doc:`../library/send_email`

