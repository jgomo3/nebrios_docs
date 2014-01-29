Checking
~~~~~~~~

The check feature allows you to set parameters that must be met in order for your action() to run. Since scripts are naturally hungry, they want to run any time their watched KVP has been created or changed. The check feature introduces a load of filtering power. For instance, only run the **order** if the **bank_account** is > $5000. We are supposing your banking system is tied into Nebri OS. A tool like http://xero.com would make that easy. 


::

    def check(self):
        return xero.bank_balance > self.order_total

Here's a standard check that doesn't reach outside the system:

::

    def check(self):
        return self.paperwork_status == "recieved"
                  

**return** is the final output of check(). In this case, it's going to return a True if bank\_balance is greater than the order\_total. A return of True means the action fires. A return of False means the script is done, and Nebri moves on to the next script. Of course these events are all logged in the admin.

Though you can run anything within check(), we don't recommend changing data since breaks command-query separation.

Since this is pure Python, you can easily query some outside service and use that in your arguments. An example might be weather temperature or status of a file transfer. It's Python!

Remember the scope of the check is only dealing with the PID that has awoken the script in the first place. That means a script check() might return false for PID 4, and true for PID 5 in the very next millisecond. 
