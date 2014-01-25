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
    :maxdepth: 2
    
    admin/index

Writing Scripts
---------------

.. toctree::
    :maxdepth: 2
    
    scripts/index

Library
-------

.. toctree::
    :maxdepth: 1
    
    library/index

Email Integration
-----------------
Learn how to instantly get full adoption by interacting with the inbox.

.. toctree::
    :maxdepth: 1
    
    email/index


Forms
-----

Forms are generally the fastest way to interact with NebriOS. With very simple scripts you can create forms that allow users in your system to accurately submit and interact with a large amount of information. It's also likely that you want to create a form for users outside your system, a survey perhaps, which is also possible. Those are called public forms. Let's see what a form looks like.

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
      

Accessing Forms
~~~~~~~~~~~~~~

There are two ways to show a form: You can click on a link from anywhere like the admin, an email, or a wiki page, or you can bring forms up automatically once a user submits an initial form. This way you can continue to click through forms and experience the flow of the application quickly, dynamically. Any mention of a form in the send\_email() for the user looking at the Interactive page will bring the very same form up in their browser. In other words, a form link will be sent to their inbox, but if they have the Interactive view open in their browser, the form that was passed to them in the email will show up right away.

The syntax for linking a form is **{{forms.example\_form}}** from inside any send\_email message. The email being sent out will render it as a full http link. This method of linking forms will be expanded once load\_form and load\_message features are introduced, but they aren't available to our users yet.

Public Forms
~~~~~~~~~~~~

Are there times you want to interact with large amount of users, but without them being an official user in your system? Think about a survey, or ordering something off a menu. These users don't need access to your system, and they will not be interacting very often with Nebri. It's best to use public forms in this case.

What's surprising is that you don't actually create a public form. Anyone is able to reach any form on your Nebri instance, in essence, but of course nothing would come up unless you had allowed it in your ACL. That means, in order to make a form public, you must make the ACL on the KVP's inside the form accessible to the public. **Just send anyone a link to your form. If the ACL allows, that's it!**

.. image:: /img/nebri_debug.jpg
                    

