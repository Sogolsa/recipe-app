from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


# UserCreationForm: built-in functionality for handling password fields and their validation.
class SignupForm(UserCreationForm):
    name = forms.CharField(max_length=120)
    picture = forms.ImageField(
        label="Profile Picture",
        required=False,
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Optional"}),
        required=False,
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    # Allows customization of help texts, which can enhance user experience.
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields["username"].help_text = "*"
        self.fields["password1"].help_text = (
            "*Your password must contain at least 8 characters and can't be entirely numeric."
        )
        self.fields["picture"].help_text = "Optional"
