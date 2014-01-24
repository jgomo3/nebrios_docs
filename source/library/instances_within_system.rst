instances\_within\_system()
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    def action(self):
        print("This action has fired "+ self.instances_within_system() +" times system wide")

When creating an action you can see if the action has already ran system-wide. This is useful to create a "singleton" type action, or make sure only an actions runs a specified number of times. For example an alarm set to notify you when stock is low could trigger a new action hundreds of times unless you check that the action in question has already ran globally anywhere in the system.



