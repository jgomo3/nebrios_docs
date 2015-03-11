============
Card Scripts
============

Nebri allows users to spawn UI's quickly with very little code. These UI's are currently in the form of "cards". A card is a `Polymer <https://www.polymer-project.org>`_ element. We chose this route because of Polymers growing momentum, their vast library of elements, and Material Design. 

There are two main routs you can take when creating Polymer elements in Nebri. The quick option is to inherit from nebrio-element and extend it with your own form fields and html. Very little code is needed to create powerful Material Design forms for your users. Many things are done automatically for you when you take this route, such as closing after it has been submitted, validation, and more. 

Nebri Cards
***********

Example card code:

.. code-block:: html

    <polymer-element name="hello-world" extends="nebrios-form" target="default.save_form">
        <template>
            <h2>Hello World</h2>
            <p>This is an example NebriOS Card.</p>
            <nebrios-string id="testy"></nebrios-string>
        </template>
        <script>            
            Polymer("hello-world", {
                });
        </script>
    </polymer-element>

Results in this card:

.. image:: /img/hello_world.png

.. note:: All card names must use **hyphens** not underscores.

The target defines which route the form fields will be saved by. In this case they hit a default api module which you can see in the API doc. More to come later about Template Cards. The following works inside the ``<template>`` tag. 


.. code-block:: html

    <nebrios-string id="string"></nebrios-string>
    <nebrios-integer id="integer"></nebrios-integer>
    <nebrios-float id="float"></nebrios-float>
    <nebrios-boolean id="boolean"></nebrios-boolean>

Optional arguments include
==========================

    * label 
        * for instruction purposes
    * required  
        * is the field required? Uses javascript.
    * defaultValue 
        * setting the starting value
    * value 
        * for databinding

Example: ``<nebrios-integer id="integer" label="Integer" required="true"></nebrios-integer>``

Validation
==========
Looking to validate inputed values before they hit your system? For example, making sure a number is within a range or an email is structured properly. Here's exactly how to do it:

.. code-block:: html

    <polymer-element name="qa-form-one" extends="nebrios-form" target="default.save_form">
        <template>
            <nebrios-string id="string" label="String" required="true"></nebrios-string>
            <nebrios-integer id="integer" label="Integer" required="true"></nebrios-integer>
            <nebrios-float id="float" label="Float" required="true"></nebrios-float>
            <nebrios-boolean id="boolean" label="boolean"></nebrios-boolean>
        </template>
        <script>
            Polymer("qa-form-one", {
                validate_string: function(field) {
                    /* only for validating the string field */
                    if (field.value.length < 4) {
                        field.error = "Name must be longer than 4 characters!";
                        return false;
                    }
                    return true;
                },
                validate: function() {
                    /* validation for ANY form field */
                    if (this.$.integer.value + this.$.float.value <= 10) {
                        this.error = "The two numbers must be greater than 10";
                        return false;
                    }
                    return true;
                }
            });
        </script>
    </polymer-element>


Manual Cards
************

The manual method allows you do anything you like within a card without being bound to the nebri-element defaults. These are just Polymer elements, so any HTML/CSS/JS that would normally work within a Polymer element is fair game. 

.. code-block:: html

    <link rel="import" href="/static/paper-slider/paper-slider.html">
    <link rel="import" href="/static/paper-item/paper-item.html">
    <polymer-element name="paper-demo" extends="nebrios-element">
        <template>
            <h2>Material Design FTW!</h2>
            <paper-slider></paper-slider>
            <core-selector>
                <paper-item>Item 1</paper-item>
                <paper-item active>Item 2</paper-item>
                <paper-item>Item 3</paper-item>
            </core-selector>
        </template>
        <script>
            Polymer("paper-demo", {});
        </script>
    </polymer-element>


And would render the following card:


.. image:: /img/material_design_form.png


Accessing Cards 
***************

Cards are seen in the default home page of your NebriOS admin. They show up automatically there for a number of reasons. Any user that is on your account experiences the same thing, except they see only the cards meant for them. Lastly, cards can be show on your Nebri url (something.nebrios.com) to public users also should you have any publicly accessible cards. 


How do you actually get a card to show? Inside of any Rule Script you can call :doc:`../builtins/load_card`. By doing this you send a card to whichever user activated the script which activated load_card().

