
Writing Nebry Scripts
=====================

A few things to note about scripts:

-  Scripts must be called into action through a KVP change in the system. They don't act otherwise.
-  As long as your script is listening to something that changes, and it's check is True, it will run.
-  Scripts don't call or reference other Nebri OS scripts, but events trigger them.

.. figure:: /img/nebri_editor.jpg
   :align: center
   :alt: 

This section will provide an overview of how to write Nebri Scripts.
 **If you would a more detailed step-by-step tutorial on writing Nebri Scipts, `read more here! </tutorial>`_**

Everything inside of a script can be categeorized in three groups; Registration, Check and Action.

.. toctree::
    :maxdepth: 2
    
    registration
    check
    action




Checking
~~~~~~~~

The check feature allows you to set parameters that must be met in order to run. Since scripts are naturally hungry, they want to run any time their watched KVP has been created or changed. The check feature introduces a load of power. For instance, only run the "order" command if the bank account is high enough. We are supposing your system is tied into Nebri OS, and the bank balance is available to it.

Script only gets to check() if this changes

Script only fires if check passes

::

    def check(self):
        return bank_balance > order_total
                  

"return" is a Python feature. It's the final output of check(). In this case, it's going to return a True if bank\_balance is greater than the order\_total.

You can run anything in this function. We don't recommend changing data during a check(), since that is considered breaking command-query separation.

Since this is pure Python, you can easily query some outside service and use that in your arguments. An example might be weather temperature or status of a file transfer. It's Python!

**Read more: `Writing Scripts - Check Method </tutorial#check_method>`_**

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

**Read more: `Writing Scripts - Action Method </tutorial#action_method>`_**

Process Contracts
~~~~~~~~~~~~~~~~~

There are two main types of Nebri script architecture. **Process scripts** monitor fewer things but usually make more changes. These allow you to make traditional processes quickly, and with extreme logical engineering. **Process Contract** is a defensive, robust-ifying type of script that adds assurance to your process. These type of scripts have a broader listens\_to scope, and will send reports or alerts if something looks off. No new syntax required, it's just the scope and parameters used.

Power alert! Process Contract scripts act as watchdogs. They monitor and report over a broad range of KVPs in the system, and help ensure the system is working as you expect. Think of them as contracts between you and the system. Some examples of scripts that would fall into this category:

-  Check if any sales process (any PID with a KVP of lead := True) has been idle for over a week.
-  Verify no new candidates are outright rejected if their test was over 95%
-  Check that the alarm in the building is never on when you are there. (Supposes integration of course)
-  Verify a customer never has a project kickoff meeting without having a verified payment method.

Since Nebri OS allows you to work with the environment without the constraints of a process, it's mind boggling how much assurance can be built into a system.

Scripting Reference
-------------------

schedule[]
~~~~~~~~~~

These are related to `Drips <#Drips>`_ but are quite different. Schedules allow you to wake a script up on a repeating schedule and try to run against **EVERY** PID in the system. This is useful for monitoring processes within your system, making sure they are moving along, aren't missing anything, and for many other uses.

**Read more: `Writing Scripts - Schedule </tutorial#schedule>`_**

required()
~~~~~~~~~~

This feature allows you to define in a script certain KVP values which **must** be available to the script before it continues forward. An example would be a list of paperwork. Each item must be inputted into the system before the script moves forward.

If the required KVPs aren't there when the script executes, it sends an email back to the last actor telling them they missed certain information.

**Read more: `Writing Scripts - Required </tutorial#required>`_**

instances\_within\_process()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    def action(self):
        print("This action has fired "+ self.instances_within_process() +" inside this PID")

When creating an action you can see if the action has already ran, relative to the process you are standing in. This is useful to create a "singleton" type action, or make sure only an actions runs a specified number of times. For example an alarm set to notify you when stock is low could trigger a new action hundreds of times unless you check that the action in question has already ran for that PID. **instances\_within\_process** is for checking all the occurrences of the action within a single processes id. **instances\_within\_system** checks system wide, no matter the process ID.

instances\_within\_system()
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    def action(self):
        print("This action has fired "+ self.instances_within_system() +" times system wide")

When creating an action you can see if the action has already ran system-wide. This is useful to create a "singleton" type action, or make sure only an actions runs a specified number of times. For example an alarm set to notify you when stock is low could trigger a new action hundreds of times unless you check that the action in question has already ran globally anywhere in the system.

send\_email()
~~~~~~~~~~~~~

::

     # all params
    send_email(TO,MESSAGE [,SUBJECT,PID,ATTATCH_VARIABLES])

    # example
    send_email("ted@examples.com", '''Hey Ted! Can I get approval for the shipments?''')

A very important feature of NebriOS is the ability to send email without any hassle. The syntax has been kept simple, and some powerful options built in. Here's additional usage examples:

::


    # sending to multiple people 
    send_email("fred@examples.com, wilma@example.com, dino@email.com", 
        '''Hey Team! Can I get approval for the shipments?''')

    # Additional arguments include subject:
    send_email(TO,MESSAGE,"Subject Here (PID:%s)" % self.different_pid)
    # This isn't ideal, and will be cleaned up in the future, but you have to reference the PID in the subject or else it doesn't get sent in the email. You are free to add whatever else you like to the subject.

    # And PID
    send_email(TO,MESSAGE,SUBJECT, PID)
    # The PID argument allows you to change which PID the KVP's at the bottom of the email gets loaded from.

**to** can contain any number of comma separated email addresses. **message** can contatain anything within tripples quotes, along with being able to pring kvp's using brackets {{like\_this}}. If you don't want to show all the kvp's in the emails, send **attatch\_variables=False**. By default it's set to true.

process\_started\_time
~~~~~~~~~~~~~~~~~~~~~~

This shows the time, as a timestamp, when the PID you are standing in was started. It's useful for understanding how long a process has been going on and reacting to it with other rules.

::

    def action(self):
        print self.process_started_time


