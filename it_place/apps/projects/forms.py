from django.forms import ModelForm
from django import forms
from .models import Event
from django.contrib.admin import widgets


class EventCreationForm(ModelForm):

    class Meta:
        model = Event
        fields = (
            "title",
            "type",
            "img",
            "specialty",
            "city",
            "about",
            "facebook",
            "instagram",
            "twitter",
            "vk",
        )

    # def __init__(self, *args, **kwargs):
    #     super(EventCreationForm, self).__init__(*args, **kwargs)
    #     self.fields['date_start'].widget = widgets.AdminSplitDateTime()
    #     self.fields['date_end'].widget =

