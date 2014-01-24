Process Contracts
~~~~~~~~~~~~~~~~~

There are two main types of Nebri script architecture. **Process scripts** monitor fewer things but usually make more changes. These allow you to make traditional processes quickly, and with extreme logical engineering. **Process Contract** is a defensive, robust-ifying type of script that adds assurance to your process. These type of scripts have a broader listens\_to scope, and will send reports or alerts if something looks off. No new syntax required, it's just the scope and parameters used.

Power alert! Process Contract scripts act as watchdogs. They monitor and report over a broad range of KVPs in the system, and help ensure the system is working as you expect. Think of them as contracts between you and the system. Some examples of scripts that would fall into this category:

-  Check if any sales process (any PID with a KVP of lead := True) has been idle for over a week.
-  Verify no new candidates are outright rejected if their test was over 95%
-  Check that the alarm in the building is never on when you are there. (Supposes integration of course)
-  Verify a customer never has a project kickoff meeting without having a verified payment method.

Since Nebri OS allows you to work with the environment without the constraints of a process, it's mind boggling how much assurance can be built into a system.

