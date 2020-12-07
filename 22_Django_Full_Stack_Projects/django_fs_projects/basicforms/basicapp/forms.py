from django import forms
from django.core import validators

# My own custom validator to check for name field - must start with 'z'
# def check_for_z(value):
#     if value[0] != 'z':
#         raise forms.ValidationError("name must start with z!")

class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])  # We defined check_for_z above!
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    # Input to catch bots, input is hidden, so human won't fill in this one!
    # validators help stop form submissions and post error back on form itself
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                    validators=[validators.MaxLengthValidator(0)])  # meaning if length of field > 0 raise exception

    # Commenting this out since we will be using django's validators (above) to catch bots!
    # Method to catch bots, if they send data in our hidden form field
    # We will use Django's methods for it but for now, doing it manually
    # Note: method name format must be: <clean>_<field_name> !
    # When we go to browser, add an attribute like value="sneaky" by dev tools in chrome, we will see nothing
    # getting to server, since we are raising an exception as below.
    # def clean_botcatcher(self):
    #     bot_text = self.cleaned_data['botcatcher']
    #     if len(bot_text) > 0:
    #         raise forms.ValidationError("GOTCHAT BOT!!")
    #     return bot_text

    # This method cleans entire form!
    # This gave me KeyError on 'email' - TODO: find out why?
    def clean(self):

        all_clean_data = super().clean()

        # Now you can grab all clean data at once!
        if 'email' in all_clean_data.keys() and 'verify_email' in all_clean_data.keys():
            email = all_clean_data['email']
            verify_email = all_clean_data['verify_email']
            if email != verify_email:
                raise forms.ValidationError("Emails must match!")
