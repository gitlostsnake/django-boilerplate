from .models import *


def contact_us_message_filter(name, email, subject, message):
    message = ContactUsMessage.objects.filter(
            name=name).filter(
            email=email).filter(
            subject=subject).filter(
            message=message
        )
    