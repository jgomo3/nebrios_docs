=====
Forms
=====


Forms are generally the fastest way to interact with NebriOS. With very simple scripts you can create forms that allow users in your system to accurately submit and interact with a large amount of information. It's also likely that you want to create a form for users outside your system, a survey perhaps, which is also possible. Those are called public forms. Let's see what a form looks like.

Here's an `example form <https://demo.nebrios.com/interact/hello_form>`_ and here's the `code <https://scripts.nebrios.com/adamnebbs/demo-form-with-every-option/>`_ it took to produce it. The following is a typical form that we use internally:

.. image:: /img/nebri_task_form.jpg

An minimal form might look like this:

::

    class my_form(Form):
        first_name = String()
        age = Number()

And would render the following form:


.. image:: /img/nebri_my_form.jpg

Available Options
=================

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
===============

There are a few ways forms show up: 

You can click on a link from anywhere like the admin, an email, or a wiki page, or you can bring forms up automatically once a user submits an initial form. This way you can continue to click through forms and experience the flow of the application quickly, dynamically. Any mention of a form in the :doc:`../library/send_email` for the user looking at the Interactive page will bring the very same form up in their browser. In other words, a form link will be sent to their inbox, but if they have the Interactive view open in their browser, the form that was passed to them in the email will show up right away.

Syntax from inside send_email:

::

    {{forms.example_form}}

Also, the email will still be sent out, and it will render the form as a full http link. This method of linking forms will be expanded once load\_form and load\_message features are introduced. Sit tight!

Public Forms
============

Are there times you want to interact with large amount of users, but without them being an official user in your system? Think about a survey, or ordering something off a menu. These users don't need access to your system, and they will not be interacting very often with Nebri. It's best to use public forms in this case.

What's surprising is that you don't actually create a public form. Anyone is able to reach any form on your Nebri instance, in essence, but of course nothing would come up unless you had allowed it in your ACL. That means, in order to make a form public, you must make the ACL on the KVP's inside the form accessible to the public. **Just send anyone a link to your form. If the ACL allows, you have a public form!**. See :doc:`../admin/acl`. 


Understanding Context
=====================

If you click on link to a form from the admin, you will be creating a new PID, as apposed to having a form brought up for you within a processes already in motion. 

Links to forms, especially from outside of Nebri, might have an associated PID encoded in the URL. For example in a form link from an email. If it doesn't have any PID in the url, it will create a new PID once info is submitted through it.

                    
 
    

