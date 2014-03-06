lists
=====

Lists are supported inside of KVP's. This way you can store any data inside of a KVP that Python would normally allow. There are some tradoffs to this approach. 

* The list is seen as a single KVP
* Nebri doesn't care about the data types in a list
* listing to a list means a trigger will happen when any part of the list is changed

In this example we take KVP's and write them to a list for storage:

::

    rd = {'user': self.last_actor,
          'work_days': self.remote_work_days,
          'date': self.date_of_remote_workd')}

See Python `documenation on lists <http://docs.python.org/2/tutorial/datastructures.html> `_ for indepth info.
