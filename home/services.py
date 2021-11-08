from .models import *

def contact_us_message_create(name, email, subject, message):
    m = ContactUsMessage()
    m.name = name
    m.email = email
    m.subject = subject
    m.message = message
    m.save()

    