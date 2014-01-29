*************
send\_email()
*************

.. code-block:: python

    # all params
    send_email(TO,MESSAGE [,SUBJECT,PID,ATTATCH_VARIABLES])

    # example
    send_email("ted@examples.com", '''Hey Ted! Can I get approval for the shipments?''')

A very important feature of NebriOS is the ability to send email without any hassle. The syntax has been kept simple, and some powerful options built in. Here's additional usage examples:

::


    # sending to multiple people 
    send_email("fred@examples.com, wilma@example.com, dino@email.com", 
        '''Hey Team! Can I get approval for the shipments?''')

    # Additional arguments include subject:
    send_email(TO,MESSAGE,"Subject Here (PID:%s)" % self.different_pid)
    # This isn't ideal, and will be cleaned up in the future, but you have to reference the PID in the subject or else it doesn't get sent in the email. You are free to add whatever else you like to the subject.

    # And PID
    send_email(TO,MESSAGE,SUBJECT, PID)
    # The PID argument allows you to change which PID the KVP's at the bottom of the email gets loaded from.


Parameters
##########


to
**
Who are you sending the email to? Can contain any number of comma separated email addresses. Eventually you will be able to use groups and usernames in this field, but not yet.

**message** can contatain anything within tripples quotes, along with being able to pring kvp's using brackets {{like\_this}}. If you don't want to show all the kvp's in the emails, send **attatch\_variables=False**. By default it's set to true.

attactch\_variables
