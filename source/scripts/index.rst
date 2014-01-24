
Writing Nebry Scripts
=====================

A few things to note about scripts:

-  Scripts must be called into action through a KVP change in the system. They don't act otherwise.
-  As long as your script is listening to something that changes, and it's check is True, it will run.
-  Scripts don't call or reference other Nebri OS scripts, but events trigger them.

.. figure:: /img/nebri_editor.jpg
   :align: center
   :alt: 

This section will provide an overview of how to write Nebri Scripts.
 **If you would a more detailed step-by-step tutorial on writing Nebri Scipts, `read more here! </tutorial>`_**

Everything inside of a script can be categeorized in three groups; Registration, Check and Action.

.. toctree::
    :maxdepth: 2
    
    registration
    check
    action







Scripting Reference
-------------------




