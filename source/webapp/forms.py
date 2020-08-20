from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from .models import STATUS_CHOICES, TYPE_CHOICES, Type, Status, Article

default_status = STATUS_CHOICES[0][0]
default_type= TYPE_CHOICES[0][0]


class AskForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['description', 'full_description', 'status', 'type', 'date' ]
        widgets = {'date': forms.DateInput(attrs={'type':'date'})}

    def clean_description(self):
        description = self.cleaned_data['description']

        if len(description) <= 2:
            raise ValidationError('Title is too short!')

        return description


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")