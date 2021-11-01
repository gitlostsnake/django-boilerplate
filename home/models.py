from django.db import models

# Create your models here.
class ContactUsMessage(models.Model):
    name = models.CharField(null=True, max_length=200)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.TextField()
    time_sent = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)

    def __str__(self):
        string = f"Message from {self.email} at {self.time_sent}"
        return string
 