Executing
~~~~~~~~~

Anything under the action() function gets executed if the script is woken up (based on what it listens\_to), AND the check() has returned True. There is where emails are sent, logic is evaluated, APIs are called, forms are called, other KVPs are set or anything else you want Python to do.

Here's a simple action you can execute. Send an email to someone letting them know how to keep the work flow going. 


.. code-block:: python

    def action(self)
        send_email("arron@example.com", "Please submit the form so I can be done with this!")

You can set KVP's at the same time.

.. code-block:: python

    def action(self)
        send_email("arron@example.com", "Please submit the form so I can be done with this!")
        self.arron_notified == True



Example gtalk plugin

.. code-block:: python

    def action(self)
        send_email("arron@example.com", "Please submit the form so I can be done with this!")
        self.arron_notified == True
        gtalk.send("arron.bixly", """Did you submit the form yet?""")
                 

Once you have a listens\_to, check() and an action(), you have the general body of a script.

In Depth
========

Checkout these tools to dive further into the possibilities.

:doc:`../builtins/send_email`

