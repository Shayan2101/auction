from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SigninForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    # To ensure that the email entered by a user during the signup process does not already exist in another account
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email
