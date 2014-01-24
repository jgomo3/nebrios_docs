===============
Using the Admin
===============

The admin website allows you to write scripts, monitor KVPs, understand what processes have been started (and why), set permissions for users, and many other things. You might be looking for a graphical overview of a process, like a BPMN representation with bubbles grayed out that have already been executed. That type of view does not exist, and cannot exist, since processes aren't technically defined in any one place. With the advent of Process Contracts, and Event Based scripting, power lies by creating assurance from various angles. It's a visibility vs. assurance issue.

.. figure:: /img/nebri_dashboard.jpg
   :align: center
   :alt: 

Debug Mode
~~~~~~~~~~

This view is only available to admins within the system. It's a tremendous help when authoring scripts. When the system has executes anything in association with your email address, you will get to see what script was triggered, what triggered it, what changed before and during the script execution, and much more. Within a few minutes you can write a script and fully test it.

The Email window basically spoofs an email client. You can quickly send in KVPs like foo := bar. It's the same syntax when writing emails. The system console will then show, realtime, what the system is doing in reaction to your changes.

Even when you are working with forms it's great to keep the debug window open. It will tell you when a script fired, if the check() passed or not, what KVP's got modified as a result, and other things.

Access Control List (ACL)

This is where you can define who can access which KVPs on your system. When a user is disallowed from viewing a KVP, it will not show up in any email or communication to them. Nor will they have access to modify it. An example of an ACL setting is to protect employees from seeing the pay\_rate of a new hire.

.. figure:: /img/nebri_acl.jpg
   :align: center
   :alt: 

Users And Groups
~~~~~~~~~~~~~~~~

Adding a user here will by default allow them to interact with your system. This way they can send emails and interact with processes in action, or trigger new process instances.

You can add users to groups, which is used for convenience in other parts of the admin, like the ACL settings.

If you mark a user as an admin, they will have privileges over everything in the administration side of the website, just like you. Usually only a couple admins are necessary, while many standard users are normal.

KVPs
~~~~

KVPs are the heart of Nebri OS. No script ever triggers unless a KVP is added or changed. If you were hiring a new employee, and built a process to help that along, you might have the following key/value pairs:

::

    first_name := Ted
    last_name := Halogen
    w9_status := Waiting
    orientation_status := finished

It's a very simple database table that stores a key value pair, or KVP. Anything in the system can adjust the KVPs, or add more, according to your ACL rules. The KVP can be any string, integer, date, url, anything you can type with your keyboard.

Any time a KVP is added or edited through the admin, by another script, an email, or anything else, it creates a signal that is put in the queue to be processed. That means a change never goes unnoticed. Thus, if you have a script watching a KVP, it will always work.

Types are dynamically set based on the content. Thus, an integer is seen as such, just as a regular word is parsed as a string. Our types are determined based on Python's preferences of course.

PID Info
~~~~~~~~

The best way to know about the state of your system is to look through the KVP table. If you click on the PID, you will see a filtered view, showing only the KVPs that pertain to that PID. It's a quick way to understand the state of a given process.

Quarantine
~~~~~~~~~~

This is a place where all your sick scripts go. If ever a script is triggered and unable to completely run because of some error, you will fine it listed in the quarantine. There you will see the script name and time of error, along with the error message that was generated.

It gets better! Once the script is updated in any way (probably in hopes of fixing the error), it's triggered again to try and run and the old quarantine is deleted. Should the script happen to error again, it will create a new entry. Otherwise, you are good to go.

Drips
~~~~~

You might think of drips as a cron on your system, but much more simple. Drips **only** allow you to set a schedule for updating KVPs. That's it. They are meant for introducing a new variable to the system so that the scripts already present can handle the rest. An example might be a meeting reminder. A drip might be set for every Tuesday that creates the KVP meeting\_today := True. It will create a new PID for each drip.

`Schedules <#Schedule>`_ are defined in scripts. They allow you to define a time when the script will wake up and try to run against every PID in the system. Related, but very different.


