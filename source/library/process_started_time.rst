process\_started\_time
~~~~~~~~~~~~~~~~~~~~~~

This shows the time, as a timestamp, when the PID you are standing in was started. It's useful for understanding how long a process has been going on and reacting to it with other rules.

::

    def action(self):
        print self.process_started_time


