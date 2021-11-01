from django.contrib.auth.models import User


def find_user_on_email(email):
    user_query = User.objects.filter(email=email)
    return user_query[0]

