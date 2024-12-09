from django import forms
from .models import PesananJasa

class PesananJasaForm(forms.ModelForm):
    class Meta:
        model = PesananJasa
        fields = ['subkategori', 'sesi_layanan', 'pekerja', 'diskon']
        widgets = {
            'status': forms.HiddenInput(),
        }
