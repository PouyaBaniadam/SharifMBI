from django import forms

from Diagnose.models import Diagnose


class DiagnoseForm(forms.ModelForm):
    class Meta:
        model = Diagnose
        fields = ("file",)
