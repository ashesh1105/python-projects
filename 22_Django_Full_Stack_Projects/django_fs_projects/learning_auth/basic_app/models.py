from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # This connect this class to User class, we are going to add attributes in our version of User class
    # Note: this is not exactly extending the User class1
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # additional attributes for users
    portfolio_site = models.URLField(blank=True)

    # We already defined a 'media' folder in settings.py for user uploaded media, (similar to 'static' for our app contents)
    # For below line, we need to ensure there's 'profile_pic' folder inside the 'media' folder!
    # Also install pillo library to manage user uploaded media by: pip install pillow
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
