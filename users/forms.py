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


class ProfileUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label="Username")

    class Meta:
        model = CustomUser
        fields = ["name", "picture", "bio"]
        widgets = {
            "bio": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Tell us about yourself..."}
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["username"].initial = user.username

    def save(self, commit=True):
        """Update the User instance along with CustomUser."""
        user = self.instance.user
        if user:
            user.username = self.cleaned_data["username"]
            if commit:
                user.save()
        return super().save(commit=commit)
