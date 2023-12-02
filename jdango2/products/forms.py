from django import forms

from jdango2.products.models import FormModel


class FormModelForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = ['username', 'age', 'comment']
