KVPs
~~~~

KVPs are the heart of Nebri OS. No script ever triggers unless a KVP is added or changed. If you were hiring a new employee, and built a process to help that along, you might have the following key/value pairs:

::

    first_name := Ted
    last_name := Halogen
    w9_status := Waiting
    orientation_status := finished

It's a very simple database table that stores a key value pair, or KVP. Anything in the system can adjust the KVPs, or add more, according to your ACL rules. The KVP can be any string, integer, date, url, boolean, and so on.

Any time a KVP is added or edited through the admin or by another script, an email, or anything else, it creates a signal that is put in the queue to be processed. That means a change never goes unnoticed. Thus, if you have a script watching a KVP, it will always work.

Types are dynamically set based on the content. Thus, an integer is seen as such, just as a regular word is parsed as a string. Our types are determined based on Python's preferences of course.

