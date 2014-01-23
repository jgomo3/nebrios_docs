==============
Nebri OS Guide
==============

Documentation to help you quickly setup Nebri OS.

Overview
--------

Scripts, KVPs, Forms and the Inbox. These are the major pieces of Nebri OS. Scripts are authored through a text editor in the admin area. Adding just a few commands to a Python script inside the Nebri OS environment allows you to create powerful "processes" quickly. Nebri OS is different, and here are a few bullet points to summarize:

-  As long as your script is listening to something that changes, and it's check is True, it will run.
-  Think in terms of principles and rules rather that the flow
-  Scripts are called into action through a KVP change in the system.
-  Users interface through their inbox, online forms, or other software hooked up to Nebri.
-  Scripts don't call other Nebri OS scripts. They only run when an event happens.
-  Because of this logical power, BPA, Contracts, CEP and others happen naturally.

The power that the Nebri OS paradigm provides is extreme, but it's important to understand some of the main features of the tool before moving on. Traditional BPM systems revolve around a process, while Nebri OS revolves around scripts that react to events. Think about an army of minions, each with a single role of operation and single assignment.

A traditional BPMN process can be replaced with a set of scripts. The power is that you don't need a predefined process, you just need to understand a nugget of functionality that you want: When the warehouse stock falls below 100, email this person, and setup an order.

It takes a little while to wrap your mind around it, because tasks/scripts interact with the environment, not a process or other Nebri OS scripts. One problem that we solved by taking this angle is that we never have a problem communicating across various processes in action since it's just the environment. This paradigm allows you to modify "processes" on the fly with zero side effects, and build your library of scripts up organically.


using the admin
---------------

.. toctree::
    :maxdepth: 1
    
    admin/admin

Writing Scripts
---------------

.. toctree::
    :maxdepth: 3
    
    scripts/index


Processes And Your Inbox
------------------------

The Inbox is the easiest path to organizational integration. Emails are sent to the system (e.g. acme@nebrios.com) and KVPs extracted and entered. Anything in the format of "foo := bar" will be entered into the system as a KVP. See, each email that is sent into Nebri OS is either A) initializing a process if it didn't exist yet, or B) responding to a process or modifying one already in motion. You will know what process you are interacting with because the Process ID will show up in the subject line. (PID:15) would tell us that PID 15 is the process we are in.

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

Forms
-----

Forms a gernerally the fastest way to interact with NebriOS. With very simple scripts you can create forms that allow users in your system to accuratly submit and interact with a large ammount of information. It's also likely that you want to create a form for users outside your system, a survey perhaps, which is also possible. Those are called public forms. Let's see what a form looks like.

Here's an `example form <https://demo.nebrios.com/interact/hello_form>`_ and here's the `code <https://scripts.nebrios.com/adamnebbs/demo-form-with-every-option/>`_ it took to produce it.

Forms are written in the forms area that you can find in the left navigation. An minimal form might look like this:

::

    class my_form(Form):
        first_name = String()
        age = Number()

Available Options
~~~~~~~~~~~~~~~~~

Here's another example form with inline comments. You can copy the script into your environment to see what it will look like, or `see it live <https://demo.nebrios.com/interact/explainer_form>`_ right now.

::

    class explainer_form(Form):

        # validation for any form field is possible
        # will warn the user if it's raised
        def validate_10_scale(form, field, value):
            if (value < 0) or (value > 10):
                raise ValidationError('Value must be between 1 and 10')

        # if you want to override the default title (the class name)
        form_title = "Tutorial Form"

        form_instructions = "I can put comments here about what you should do on the form."



        # 'name' here will turn into a KVP and recieve any value
        # that is collected from this form
        name = String()

        # labels print above the form box
        age = Number(label="Provide your age")

        # initial will fill in the value upon loading
        # you can fill it with other KVP's also
        favorite_number = Number(initial=42)

        # validation points to a function you have written
        # if it can't pass validation it is sent back to the user
        # for example, can't be above 10 or below zero
        ice_cream_rating = Number(message="1-10 - How much do you like Ice Cream?", validation=validate_10_scale)


        # some fields are very important, so mark them as required.
        you_are_alive = Boolean(required=True)

        # bools can be dropdowns also
        bool_drop_down = Boolean(initial=False, dropdown=True)

        # or radio
        bool_radio = Boolean(initial=False, radio=True)

        # combo box as a string
        combo_box_string = String(choices=[('AK', 'Arkansas',),('CA', 'California',)])

        # combo box as a number
        combo_box_number = Number(choices=[(1, 'One',),(2, 'Two',)])

        # allow multiple selectection
        multi_box_one = String(choices=[(1, 'One',),(2, 'Two',)], multiselect=True)

        # date/time selection and input
        when = DateTime(initial=datetime.now())

        # time selection only
        requested_time = Time(initial=datetime.now())
      

Acessing Forms
~~~~~~~~~~~~~~

There are two ways to show a form: You can click on a link from anywhere like the admin, an email, or a wiki page, or you can bring forms up automatically once a user submits an initial form. This way you can continue to click through forms and experience the flow of the application quickly, dynamically. Any mention of a form in the send\_email() for the user looking at the Interactive page will bring the very same form up in their browser. In other words, a form link will be sent to their inbox, but if they have the Interactive view open in their browser, the form that was passed to them in the email will show up right away.

The syntax for linking a form is **{{forms.example\_form}}** from inside any send\_email message. The email being sent out will render it as a full http link. This method of linking forms will be expanded once load\_form and load\_message features are introduced, but they aren't available to our users yet.

Public Forms
~~~~~~~~~~~~

Are there times you want to interact with large amount of users, but without them being an official user in your system? Think about a survey, or ordering something off a menu. These users don't need access to your system, and they will not be interacting very often with Nebri. It's best to use public forms in this case.

What's surprising is that you don't actually create a public form. Anyone is able to reach any form on your Nebri instance, in essence, but of course nothing would come up unless you had allowed it in your ACL. That means, in order to make a form public, you must make the ACL on the KVP's inside the form accessible to the public. **Just send anyone a link to your form. If the ACL allows, that's it!**

.. |image0| image:: img/nebri_debug.jpg
                    

