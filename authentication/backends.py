from django.contrib.auth.backends import ModelBackend
from .models import CustomUser
from django.contrib.auth.models import User


class CustomUserBackend(ModelBackend):
    def authenticate(username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            print("user name", user.username)
        except User.DoesNotExist:
            print("Doesnot exists")
            return None

        if user.check_password(password):
            return user
        return None
