from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        # Note: order of fields in the fields list below decide ordering of these on the forms as well that user will see!
        # https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#changing-the-order-of-fields
        fields = ['username', 'email', 'password']

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ['portfolio_site', 'profile_pic']
