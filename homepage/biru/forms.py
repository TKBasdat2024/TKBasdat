from django import forms

from .models import Testimoni


class TestimoniForm(forms.ModelForm):
    class Meta:
        model = Testimoni
        fields = ['konten', 'rating']
        widgets = {
            'konten': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }
