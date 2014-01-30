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



.. toctree::
    :maxdepth: 2
    
    scripts/index

.. toctree::
    :maxdepth: 2
    
    admin/index

.. toctree::
    :maxdepth: 2
    
    library/index

.. toctree::
    :maxdepth: 2
    
    email/index

.. toctree::
    :maxdepth: 2

    forms/index
