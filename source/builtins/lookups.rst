*************
Field Lookups
*************

The following lookups are supported

..

  * __lt: less than
  * __lte: less than or equal to
  * __gt: greater than
  * __gte: greater than or equal to
  
  
Whether you are using our `Process ORM <http://nebridocs.readthedocs.org/builtins/process_ORM.html>`_ or `nebrios-models <https://github.com/fernandobixly/nebrios-models>`_, you may use these lookups as you would when using the Django ORM.

For your reference, imagining "date_value" is a variable containing one of our datetimes, the following code is now functional:

With Process ORM
================

.. code-block:: python

  entries = Process.objects.filter(kind="email_message", received_on__gte=date_value)

With nebrios-models
===================

.. code-block:: python

  entries = EmailMessage.filter(received_on__gte=date_value)
