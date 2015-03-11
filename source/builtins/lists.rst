lists and dicts
===============

Lists and Dictionaries are supported inside of KVP's. This way you can store any data inside of a KVP that Python would normally allow. There are some tradoffs to this approach. 

* The list/dict is seen as a single KVP
* Nebri doesn't care about the data types in a list/dict
* listining to a list/dict means a trigger will happen when anything insde it is changed

In this example we take KVP's and write them to a list and dict for storage:

.. code-block:: python

    self.my_list = []
        # first initialize the list

    self.my_list.append(self.last_actor,
        self.remote_work_days,
        self.date_of_remote_work')
        
    self.my_dictionary = {'user': self.last_actor,
      'work_days': self.remote_work_days,
      'date': self.date_of_remote_work'}

    self.my_dictionary["user"] = self.last_actor


Lists can be used inside of :doc:`shared` also. For example you might want to have a global list of log times for a certain task so you are able to query it later. Tuples are not supported. 

See Python `documenation on lists <http://docs.python.org/2/tutorial/datastructures.html>`_ for indepth info.

