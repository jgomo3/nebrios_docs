==============
API Scripts V1
==============


This document describes how to create endpoints in your Nebri instance, or consume other API's with Python scripts. An API endpoint is instantly available by creating a script in the API section of the admin or over ssh. See :doc:`../misc/folder_structure`. You can use the `nebrios-authentication <https://github.com/briem-bixly/nebrios-authentication>`_ library to use both token and basic http autentication. 

Endpoints are then reachable with this URL structure:

::

    api/vX/MODULE/FUNCTION

For example a module in your library named **form.py** with a **save()** function is available at 

::

    your_instance.nebrios.com/api/v1/form/save
    
See Python's `module <https://docs.python.org/2/tutorial/modules.html>`_ documentation. 

Consuming API's can happen from these scripts also, or another Python script anywhere in your system. Keys are handled from the user table. Here's an API script that you can use to bind any form fields to an actual KVP. 

.. code-block:: python

    def save(request):
        if request.PROCESS and request.FORM:
            for key, value in request.FORM:
                request.PROCESS[key] = value
            request.PROCESS.save()
            

The following example card would allow you to save any form field within that card to the KVP table:

.. code-block:: html

    <polymer-element name="hello-world" extends="nebrios-form" target="default.save">
        <template>
            <h2>Hello World</h2>
            <p>This is an example NebriOS Card.</p>
            <nebrios-string-field id="testy"></nebrios-string-field>
        </template>
        <script>            
            Polymer("hello-world", {
                });
        </script>
    </polymer-element>


AJAX Calls
**********

You can use AJAX from your Polymer cards to run Nebri API modules. This is useful for grabbing information from within Nebri and displaying it on the fly. For example, an API module can be used to query Shared KVP data needed by the Card. The API module simply needs to "return" whatever information needed.

Here is an example API module for grabbing a Shared KVP.
(Assuming the module name has been set as **shared_lookup**)

.. code-block:: python

    def get_company_address(request):
        return shared.company_address

    
And here's a Polymer card that calls it. Note that the **auto="true"** attribute makes the AJAX call execute immediately without user interaction.

.. code-block:: html

    <polymer-element name="show-company-name" extends="nebrios-element">
        <template>
            Company Name: {{company_name}}
            
            <nebrios-ajax id="get_company_name" auto="true"
              url="/api/v1/shared_lookup/get_company_name"
              on-response="{{ onGetCompanyNameResponse }}">  
            </nebrios-ajax>
            
        </template>
        <script>
            Polymer("ajax-math", {
                a: "0",
                b: "0",
                company_name: "",
                onGetCompanyNameResponse: function(event, response) {
                    this.company_name = response.response;
                }
            });
        </script>
    </polymer-element>


Here is another an example API module for doing some math on the Python side of things:

.. code-block:: python

    def add(request):
        sum = int(request.POST["a"]) + int(request.POST["b"])
        return sum

Call this example function from a Polymer card.  This AJAX call will not execute until the user clicks the submit button. The **this.$.do_math.go** function triggers the AJAX call.

.. code-block:: html

    <polymer-element name="ajax-math" extends="nebrios-element">
        <template>
            AJAX Math
            <br><br>
            A: <input type="text" value="{{ a }}">
            <br>
            B: <input type="text" value="{{ b }}">
            <br>
            <paper-button on-click="{{ onSubmitClick }}">Submit</paper-button>
            
            <nebrios-ajax id="do_math" auto="false"
              url="/api/v1/math/add"
              on-response="{{ onDoMathResponse }}"
              params='{"a": "{{ a }}", "b": "{{ b }}" }'>  
            </nebrios-ajax>
            
            <div>{{ a }} plus {{ b }} equals {{ math_result }}</div>
        </template>
        <script>
            Polymer("ajax-math", {
                a: "0",
                b: "0",
                math_result: "",
                onSubmitClick: function() {
                    this.$.do_math.go();
                },
                onDoMathResponse: function(event, response) {
                    this.math_result = response.response;
                }
            });
        </script>
    </polymer-element>
    
    
Built-Ins
=========

Card Loader
***********

You can invoke cards by using the card loader built in. It allows signed-in and public users to bring up cards and submit values through them. 

.. code-block:: python

    # format
    api/vX/cards/load?name=NAME
    
    # example
    https://example.nebrios.com/api/v1/cards/load?name=hello-world
    
Only cards with that are marked at publicaclly avaiable can be reached this way by non-authenticated users. Also, submitting KVP's are still subject to :doc:`../admin/acl`. 


Nebri User Authentication
*************************

Within an API you can check if the user who invoked the script is authenticated. This is a simple way to to keep only Nebri users from your instance using a specific endpoint, if that's what you desire. 

.. code-block:: python

    if not request.is_authenticated:
        return HttpResponseForbidden()



        
