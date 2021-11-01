from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Profile has a one to one relationship with the user. Every user will have a profile and will be triggered when a user signs up.
# accounts/signals.py has the reviever signal functions.
class Profile(models.Model):
    """Extends the defaul django user model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)


