Parent Child Processes
======================

What if you want to spawn a new PID from an existing PID? For example, you have a process in motion that orders new food items when low, but now you want to launch the freezer cleaning process and not have it effect your order process. In this case it's best launch a whole new child process. 

:: 
    
    new_child.clean_freezer == True

You will have the ability to communicate with that child process also. Maybe you want to know the status of it, but not depend on the status of it. 

::
    
    def check(self):
        return child.clean_freezer == "Done"

    def action(self):
        # notify boss: ok to book a restaurant tour
