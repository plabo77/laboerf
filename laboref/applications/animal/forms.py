from django import forms

from .models import Animal


class EditAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('name', "age", "breed", "color")


class NewAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('' 'name', "age", "breed", "color")
