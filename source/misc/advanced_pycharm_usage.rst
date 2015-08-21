Advanced PyCharm Usage
======================

`PyCharm <https://www.jetbrains.com/pycharm/>`_ is a great tool for NebriOS development, and is used for all development
at NebriOS HQ. The following guide demonstrates more advanced usage of `PyCharm <https://www.jetbrains.com/pycharm/>`_
when developing a NebriOS app, including use of third-party apps.

**Note**: all usernames, hostnames, and IP addresses have been garbled, because, um, well, the Internet.

Project Creation
----------------

Let's start with creating a new `PyCharm <https://www.jetbrains.com/pycharm/>`_ project for our NebriOS app. We shall name our app *nebrios_test_app*.

.. image:: /img/advanced_pycharm/01.png
   :target: /img/advanced_pycharm/01.png

After creating the project, we should have an empty `PyCharm <https://www.jetbrains.com/pycharm/>`_ project.

.. image:: /img/advanced_pycharm/02.png
   :target: /img/advanced_pycharm/02.png

SFTP Setup
----------

Let's set up SFTP with the project, in order to be able to copy files over to our NebriOS instance from `PyCharm <https://www.jetbrains.com/pycharm/>`_.

.. image:: /img/advanced_pycharm/03.png

Click on the *settings* button on the *Remote Host* tool window.

.. image:: /img/advanced_pycharm/04.png

The *Add Server* dialog appears, requesting a name for the SFTP server.

.. image:: /img/advanced_pycharm/05.png

In the Connection tab, provide host IP, port, username, and password as specified in your NebriOS Welcome Email.
**Note**: the root path is */home/nebrios-sftp* for all NebriOS instances.

.. image:: /img/advanced_pycharm/06.png

After setting up the connection, click on the Mappings tab and set Deployment and Web paths to */*. Make sure to click
the *Use server as default* button.
**Note**: the Web path is not really important, since NebriOS is not exactly a webserver, but it does make `PyCharm <https://www.jetbrains.com/pycharm/>`_
warnings disappear.

.. image:: /img/advanced_pycharm/07.png

.. image:: /img/advanced_pycharm/08.png

After clicking *OK*, `PyCharm <https://www.jetbrains.com/pycharm/>`_ will connect to the SFTP host you have set up. You should see the contents of your NebriOS
instance.

.. image:: /img/advanced_pycharm/09.png

One nice side effect of setting up SFTP with `PyCharm <https://www.jetbrains.com/pycharm/>`_, is that you can now also easily connect to your instance over
SSH, which is useful for, say, installing python libraries using PIP. To connect to your instance over SSH, click
*Tools | Start SSH session...*

.. image:: /img/advanced_pycharm/11.png

The *Select host to connect* context menu will appear. After clicking on your instance, `PyCharm <https://www.jetbrains.com/pycharm/>`_ will open an SSH
connection which will be accesible from the *Terminal* tool window.

.. image:: /img/advanced_pycharm/12.png

Finally, let us copy the app to our instance, by right-clicking on the *nebrios_test_app* folder, then clicking on
*Upload to <instance name>*.

.. image:: /img/advanced_pycharm/13.png

Third-party NebriOS Apps
------------------------

A NebriOS App is a collection of folders with Python modules, Polymer elements, and other miscellaneous support files
needed by app in question. Apps have the following file/folder structure:

    - /api: Contains :doc:`API Scripts </api/index>` (Python modules)

    - /card_html_files: Contains :doc:`../cards/index` (HTML files)

    - /libraries: Contains Python modules directly importable by name in *API* or *Rule scripts* (Python Modules)

    - /scripts: Contains :doc:`../rules/index` (Python modules)

    - /workspace: Contains miscellaneous files required by the app - files residing in this folder can be opened without specifying a path (ie. for a file named *image.png*, it can be opened in a script by using ``f = open('image.png')``.

    - README.md: App documentation

NebriOS Apps do not need to have all of these folders: only folders containing at least one file are required. At
NebriOS HQ, we have a modest but growing list of free third-party apps, and these usually come in the form of Github
repos.

Let's start our foray into third-party apps with `nebrios-models <https://github.com/fernandobixly/nebrios-models/>`_,
which provides *models* as a paradigm to handle NebriOS Processes.

Checkout the *nebrios-models* app from `PyCharm <https://www.jetbrains.com/pycharm/>`_.

.. image:: /img/advanced_pycharm/14.png

Provide the HTTPS clone url to the *Clone repository* dialog.

.. image:: /img/advanced_pycharm/15.png

Click yes on the *Checkout from Version Control* dialog.

.. image:: /img/advanced_pycharm/16.png

Set up options as shown on the *Open Project*, then click *OK*.:align:

.. image:: /img/advanced_pycharm/17.png

After opening the project, let's click on the *settings* button in the *Remote Host* tool window, select our
instance, and then click on the *Mappings* tab, where we will find an issue which we must fix.

.. image:: /img/advanced_pycharm/18.png

After clicking on *Fix* in the previous window, set the *Deployment* and *Web* paths for the new app, then click *OK*.

.. image:: /img/advanced_pycharm/19.png

.. image:: /img/advanced_pycharm/20.png

**Note**: Marking folders as *Sources roots* allows `PyCharm <https://www.jetbrains.com/pycharm/>`_ to provide importing and other auto-complete/inspection
information from your project. This is only necessary for folders containing Python modules. To mark folders as *Sources
Roots*, right click on the folder in question, hover over *Mark Directory As*, then click *Sources Root*.

.. image:: /img/advanced_pycharm/21.png

Debugging Tricks
----------------

After setting up our app, we now add some code. Let's add a *library module* named *nebrios_test_models*, to define a
model that we shall use in a script.

.. image:: /img/advanced_pycharm/22.png

Let's also create a :doc:`Rule script </rules/index>` named *test_script*.

.. image:: /img/advanced_pycharm/23.png

After creating the files, let's copy our app the *nebrios_test_app* folder **only** (as shown on the *SFTP Setup*
section), and let's visit our NebriOS instance's :doc:`../admin/debug_mode` page to submit a :doc:`KVP </admin/kvps>` that will wake up our rule script.

.. image:: /img/advanced_pycharm/24.png

After submitting the :doc:`KVP </admin/kvps>`, we will notice that an error occurred during :doc:`Rule script execution </rules/action>`, because we failed to import
the module where we defined our model.

.. image:: /img/advanced_pycharm/25.png

Exceptions in :doc:`Rule script </rules/index>` execution generate :doc:`Quarantines </admin/quarantine>`, which save a particular attempt at execution, and allow you to
rerun the same exact operation on the same PID after changing the :doc:`Rule script </rules/index>` in question. **Note**: the contents of
the script **MUST** change in order for a :doc:`../admin/quarantine` to attempt rerunning the script.

With this in mind, lets fix the issue by importing the required module in our *test_scrpt*.

.. image:: /img/advanced_pycharm/26.png

After editing *test_script* and looking at :doc:`../admin/debug_mode` for a few seconds, we may notice that *test_script* does not
execute again, as expected from the :doc:`../admin/quarantine`. If we visit the :doc:`Rule script </rules/index>` editor page for *test_script*, we shall
find that the :doc:`../admin/quarantine` remains, and a *Syntax error* remains.

.. image:: /img/advanced_pycharm/27.png

:doc:`Quarantines </admin/quarantine>` are only run on :doc:`../rules/index` if no *Syntax errors* are found. In this particular case, we intentionally
failed to upload the *nebrios-models* app. Lets copy the *nebrios-models* app to our instance.

After again looking at :doc:`../admin/debug_mode` for a few seconds, we will notice that execution still does not occur. If we look at
the :doc:`Rule script </rules/index>` editor page for *test_script*, we will notice that the *Syntax error* remains. :doc:`../rules/index`
are only syntax-checked whenever they change, and :doc:`Quarantines </admin/quarantine>` are only attempted after detecting :doc:`../rules/index` file
changes.

Let's make a simple change in *test_script* in order to force a recheck.

.. image:: /img/advanced_pycharm/28.png

After copying *test_script* to the instance once more, you will find in :doc:`../admin/debug_mode` that the script finally executes.

.. image:: /img/advanced_pycharm/29.png