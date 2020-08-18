from django import forms
from django.core import validators
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data.get('email',None)
        vmail = all_clean_data.get('verify_email',None)
        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
