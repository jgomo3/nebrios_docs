===========
API Scripts
===========


You can quickly create endpoints to your Nebri instance, or consume other API's with Python scripts. An API endpoint is instantly available by creating a script in the API section of the admin. The endpoint is named after the script (a `module <https://docs.python.org/2/tutorial/modules.html>`_). For example a module named writer.py is available at **your_instance.nebrios.com/api/writer/**. Consuming API's can happen from these scripts, or another Python script anywhere in the system. Keys are handled from the user table. Let's get into the details!


As we transition into this new way of programming Nebri, the documentation is still playing catch up. Here's an API script that you can use to bind any form fields to an actual KVP. 

.. code-block:: python

    def save_form(request):
        if request.PROCESS and request.FORM:
            for key, value in request.FORM:
                request.PROCESS[key] = value
            request.PROCESS.save()
            

The following example card would allow you to save any form field within that card to the KVP table:

.. code-block:: html

    <polymer-element name="hello-world" extends="nebrios-form" target="default.save_form">
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
==========

You can also query any Python script in your environment via Ajax. Example API module (named math):

:: 

    def add(request):
        sum = int(request.POST["a"]) + int(request.POST["b"])
        return sum

Call this example function from a Polymer card:

::

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


        
