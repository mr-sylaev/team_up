from django.forms import ModelForm
from django import forms
from .models import Event
from apps.main.models import Reit
from django.contrib.admin import widgets


class EventCreationForm(ModelForm):
    date_start = forms.CharField(widget=forms.TextInput(attrs={'type': 'datetime-local'}),)
    date_end = forms.CharField(widget=forms.TextInput(attrs={'type': 'datetime-local'}),)

    class Meta:
        model = Event
        fields = (
            "title",
            "type",
            "date_start",
            "date_end",
            "img",
            "specialty",
            "city",
            "about",
            "facebook",
            "instagram",
            "twitter",
            "vk",

        )
class ReitForm(forms.ModelForm):
    class Meta:
        model = Reit
        fields = ('reit',)

    # def __init__(self, *args, **kwargs):
    #     super(EventCreationForm, self).__init__(*args, **kwargs)
    #     self.fields['date_start'].widget = widgets.AdminSplitDateTime()
    #     self.fields['date_end'].widget =

