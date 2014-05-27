Inbox Interaction
-----------------

The Inbox is the easiest path to organizational integration. Emails are sent to the system (e.g. acme@nebrios.com) and from the system (see  :doc:`../library/send_email`). KVP's can be sent into Nebri this way also. Anything in the format of "foo := bar" will be entered into the system as a KVP. See, each email that is sent into Nebri OS is either A) initializing a process if it didn't exist yet, or B) responding to a process or modifying one already in motion. You will know what process you are interacting with because the Process ID will show up in the subject line. (PID:15) would tell us that PID 15 is the process we are in.

To illustrate why this is important, imagine you hire on two new people. They will both have the same type of info, like first\_name, last\_name, pay\_rate for instance. But you need to be able to track information about their status separately. The first hire that you bring on can be activated from an email like this:

::

    first_name := Ted
    last_name := Halogen
    new_hire := True

If you sent that email into Nebri OS, and a script was monitoring the new\_hire KVP, things would be set in motion. Since this process is just starting, you would get an email letting you know that a new PID (let's say PID:1) was just created to accommodate the new information. Then, let's say you get another new hire, and want to start a process for her:

::

    first_name := Jill
    last_name := Nanomo
    new_hire := True

A brand new process would be created, such as PID 2. Now the lanes are clearly established, and you and other managers can fully interact with the new hires separately.

Attachments
~~~~~~~~~~~

Attachments are handled in a special way. Each attachment you email to Nebri OS gets associated with the PID in question and becomes available as a KVP. The KVP of that attachment is the URL that can be used to access the attachment by anyone privy to the process. So, if you email an attachment, the next person to interact with the PID will get an email with an additional KVP listed at the bottom of the KVP table that goes with every email. This KVP will be a link to the file that was sent in as an attachment. It will be forever available.

Composing Emails
~~~~~~~~~~~~~~~~

The rules to composing emails are actually very easy. A lot of work has been put in to ensure that any KVP can be pulled from any email. It's best to use this format: **name := value**. If multiple KVPs are found contradicting each other in the same email, the first one processed is the one that is used. Also, the KVPs can be pulled from any area of the email: the response, the main body, signature, whatever.

For documentation purposes, or just being more expressive to the other people you are cc'ing, you can do something like this:

::

    to: max@acme.com, heather@acme.com, acme@nebrios.com

    Hey Guys, 
    I just wanted to let you know I have to request more budget 
    for this next quarter because of the sales slump. Feel free
    to chat with me about it.

      additional_budget_request := 5000
      department := widgets

This allows you to interact with people and a defined structure in a natural way.

Printing KVPs
~~~~~~~~~~~~~

It's very easy to send dynamic information via email via the print syntax. Anything encompassed in double braces, {{like\_this}}, will be printed if it represents a variable/KVP within the database. Here's an example of an email that is composed from a script to be sent out to other people involved in the process:

::

    Hello HR, 
    A new employee named {{employee_name}} is now waiting to be processed.

If that variable exists in the system, for the PID in question, it will get printed in the email. If it's not available, it will just be blank. No error will be thrown to the user.

Syntax Notes
~~~~~~~~~~~~

It works like variables inside of most programming languages. If you use spaces, surround them in quotes. "this is valid". For multi line strings, put them in triple quotes. Other symbols and numbers are fine.


