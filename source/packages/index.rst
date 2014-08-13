===============
Adding Packages
===============

Adding Python packages lends tremendous power to your Nebri instance. Via pip install you have access to more than 40,000 Python packages right away. Your own packages can be uploaded with SFTP if you like also.

Connecting over SSH
~~~~~~~~~~~~~~~~~~~

Contact support for the ip address and port number to connect to. Your username and password is then used to connect. 

Connecting over FTP
~~~~~~~~~~~~~~~~~~~

Contact support for the ip address and port number to connect to. Your username and password is then used to connect. 

Example Usage
~~~~~~~~~~~~~

From inside the bash terminal you can run pip!

::

    pip install yweather

Then call it from inside your script just like so:

::

    import yweather

    class weather(NebriOS):
        listens_to = ['getweather']

        def check(self):
            return self.getweather  == True

        def action(self):
            client = yweather.Client()
            id = client.fetch_woeid("Paris, France")
            self.weather = client.fetch_weather(id)

.. note::  Avoid name clashes. Don't name your class the same as your import. 

That example code pulls directly from the Yahoo weather RSS, so no API keys or account needed. You can test that yourself right now. 

Additionally you can run Python from the terminal directly to test out the module before writing a full script for it. 

After you shell is open, start Python:

::

    python

Then import:

::

    >>>import yweather

Then instantiate the class and make the call:

::

    >>>client = yweather.Client()
    >>>id = client.fetch_woeid("Paris, France")
    >>>print client.fetch_weather(id)
