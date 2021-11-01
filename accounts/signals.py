from django.contrib.auth.models import User

from .models import Profile

# Specifically for the custom signal reciever for profiles.
from django.dispatch import receiver
from django.db.models.signals import post_save


# post_save executes every time the User is updated. Creates/updates the profile when the user is created/updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwards):
    instance.profile.save()