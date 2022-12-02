from django import forms
from . import models


class Form_text(forms.ModelForm):
    class Meta:
        model = models.Model_text
        fields = '__all__'