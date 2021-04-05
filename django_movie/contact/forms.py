from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Contact


class ContactForm(forms.ModelForm):
    """Form to sign up by email"""

    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ("email", "captcha", )
        widgets = {
            "email": forms.EmailInput(attrs={"class": "editContent"}),
        }