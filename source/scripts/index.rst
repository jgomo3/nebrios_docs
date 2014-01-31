
Writing Nebri Scripts
=====================

A few things you should know about scripts:

-  Scripts must be called into action through a KVP change in the system. They don't act otherwise.
-  As long as your script is listening to something that changes, and it's check is True, it will run.
-  Scripts are written in pure Python/Django. 

.. figure:: /img/nebri_editor.jpg
   :align: center
   :alt: 

Everything inside of a script can be categeorized in three groups; Registration - what is being listened to inside your system, Check - What conditions must be true before moving forware and Action - if everything checks out, do this.

.. toctree::
    :maxdepth: 2
    
    registration
    check
    action
    parent_child

