instances\_within\_process()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    def action(self):
        print("This action has fired "+ self.instances_within_process() +" inside this PID")

When creating an action you can see if the action has already ran, relative to the process you are standing in. This is useful to create a "singleton" type action, or make sure only an actions runs a specified number of times. For example an alarm set to notify you when stock is low could trigger a new action hundreds of times unless you check that the action in question has already ran for that PID. **instances\_within\_process** is for checking all the occurrences of the action within a single processes id. **instances\_within\_system** checks system wide, no matter the process ID.

