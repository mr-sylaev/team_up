from django.contrib.auth.forms import UserCreationForm
from .models import ItUser
from django import forms


class ItUserCreationForm(UserCreationForm):
    birth = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}), )

    class Meta:
        model = ItUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "img",
            "city",
            "birth",
            "specialty",
            "experience",
            "education",
            "about",
            "skills",
            "edu",
            "edu_list",
            "github",
            "bitbacket",
            "pinterest",
            "facebook",
            "instagram",
            "twitter",
            "vk",
        )
