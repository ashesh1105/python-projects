from django import forms
from my_app.models import User

class NewUserForm(forms.ModelForm):

    # If we want to do custom validations (apart from what we have on model), we'll define fields here
    # and add either clean method to clean entire form or custom clean method and define with spefic field
    # as validators. Check basicforms app for that! We're not doing those here for now.

    class Meta():
        model = User
        fields = '__all__'
