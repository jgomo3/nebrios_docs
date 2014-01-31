children
========

This method allows you to query all available children a parent has.

::

    # Number of children
    print len(children)

    # Iteration
    for child in children:
        # Do something with child, which is a kvp bag
        if child.paid:
            # Note use of child variable and reserved PROCESS_ID variable
            child.ticket_number += "%s-%s" % (self.PROCESS_ID, child.PROCESS_ID)

    # Filtering
    for child in children.filter(paid=True):
        child.ticket_number += "%s-%s" % (self.PROCESS_ID, child.PROCESS_ID)

    # Raises TooManyObjectsReturned exception if this search returns more than one entry
    child = children.get(paid=True)
    child.ticket_number += "%s-%s" % (self.PROCESS_ID, child.PROCESS_ID)
        
