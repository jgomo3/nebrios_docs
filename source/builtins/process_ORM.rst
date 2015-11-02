***********
Process ORM
***********

The Process ORM is modeled after Django's ORM. It allows you to fetch PID's and KVP's, and also create KVP's under existing or new PID's. These can be used both API and Rule scripts. 

get()
=====

Query one or more KVP's by PID or Value.  

.. code-block:: python
    
    Process.objects.get(PROCESS_ID=?, kvp_name=value)

    # Example usage
    p = Process.objects.get(PROCESS_ID=12, kvp_a=123)
    p.kvp_b = 456
    p.save()

get_or_create()
===============

Same as get(), but it creates a PID if it doesn't exist.

create()
========

Create KVP's. This creates a whole new PID. By contrast, when you create KVP's within a rule script (self.a = foo) you are within the PID context that script woke up under. 

.. code-block:: python
    
    p = Process.objects.create()
    p.kvp_a = 123
    p.save()
        # changes aren't saved until you call this

We will be expanding this create() to include parent and child creation in the future.  It will replace the current parent/child functionality. 


filter()
========

.. code-block:: python

    q = Process.objects.filter(PROCESS_ID=12, kvp_a=123)
    
    # supports synthetic queryset
    # call this an filter the results
    q2 = q.filter(kvp_b=33)
    
    
Nebri Models
============
Nebri Models (found `here <https://github.com/fernandobixly/nebrios-models>`_) ads the power of models to Nebri. It's a great way to wrap the Process ORM. 

Example usage:

.. code-block:: python

    try:
        user = User.get(username="testuser")
        # we can manipulate the object here
        cars = MyCar.filter(user=user)
        for car in cars:
            # We have a list of cars here
    except:
        # exception thrown if model not found
        
Lookups
=======

See :doc:`lookups`. 




