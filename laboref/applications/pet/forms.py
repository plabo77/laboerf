from django import forms

from .models import Pet


class EditPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', "age", "breed", "color")


class NewPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('' 'name', "age", "breed", "color")
