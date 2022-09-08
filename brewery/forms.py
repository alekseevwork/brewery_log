from django import forms
from .models import Measuring, Tank


class MeasuringForm(forms.ModelForm):
    class Meta:
        model = Measuring
        fields = ['tank', 'temperature', 'density', 'pressure', 'comment']
        widgets = {
            # 'tank': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'title': forms.TextInput(attrs={'class': 'form-control'}),
            'temperature': forms.NumberInput(attrs={'class': 'form-control'}),
            'density': forms.NumberInput(attrs={'class': 'form-control'}),
            'pressure': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddTankForm(forms.ModelForm):
    class Meta:
        model = Tank
        fields = ['title', 'number']
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# class DeleteTankForm(forms.ModelForm):
#     class Meta:
#         model = Tank
#         fields = ['title', 'number']
