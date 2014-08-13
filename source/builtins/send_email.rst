*************
send\_email()
*************

.. code-block:: python

    # all params
    send_email(to,message [,SUBJECT,PID,ATTATCH_VARIABLES])

    # example
    send_email("ted@examples.com", '''Hey Ted! Can I get approval for the shipments?''')

A very important feature of NebriOS is the ability to send email without any hassle. The syntax has been kept simple, and some powerful options built in. Here's additional usage examples:

::


    # sending to multiple people 
    send_email("fred@examples.com, wilma@example.com, dino@email.com", 
        '''Hey Team! Can I get approval for the shipments?''')

    # Additional arguments include subject:
    send_email(TO,MESSAGE,"Subject Here (PID:%s)" % self.different_pid)
    # This isn't ideal, and will be cleaned up in the future, but you have to 
    # reference the PID in the subject or else it doesn't get sent in the email. 
    # You are free to add whatever else you like to the subject.

    # And PID
    send_email(TO,MESSAGE,SUBJECT, PID)
    # The PID argument allows you to change which PID the KVP's at the bottom 
    # of the email gets loaded from.


Parameters
##########


to
**
    Who are you sending the email to? Can contain any number of comma separated email addresses. Eventually you will be able to use groups and usernames in this field, but not yet.

message
*******

    Your message can contain anything within triple quotes. Also, you can print KVP's inside of an email. Here' the format:

::

    send_email("ted@example.com", """Ted, you have {{draft_amount}} drafts left to deliver""")

You can also send links directly to forms:

::

    send_email("ted@example.com", """Please submit your draft with this form: {{forms.draft_uploader}}""")

If users are in the interactive mode while a form containing email is sent to them, that form will show up in their browser. It's a slight hack, but it works. We are going to introduce load\_form and load\_message soon to fix the issue.

attactch\_variables
*******************

     If you don't want to show all the kvp's in the emails, send **attach\_variables=False**. By default it's set to true.

subject
*******
    
    You can override the subject line of any email, otherwise, it will just have the PID of the email. However, doing this removes the pid of the email. See the example above for overcoming this issue.    

