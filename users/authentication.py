from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()  # Get the custom user model

class UsernameOrEmailBackend(ModelBackend):
    """
    Custom authentication backend to allow login using either email or username.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)  # Check if username is an email
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)  # Check if it's a username
            except User.DoesNotExist:
                return None

        if user and user.check_password(password):
            return user
        
        return None
