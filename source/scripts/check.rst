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

