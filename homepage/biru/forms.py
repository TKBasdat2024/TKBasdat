from django import forms

from .models import PembelianVoucher, Testimoni, Voucher


class TestimoniForm(forms.ModelForm):
    class Meta:
        model = Testimoni
        fields = ['konten', 'rating']
        widgets = {
            'konten': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }

class VoucherForm(forms.ModelForm):
    class Meta:
        model = Voucher
        fields = ['kode', 'deskripsi', 'diskon_persen', 'tanggal_mulai', 'tanggal_berakhir']
    
class PembelianVoucherForm(forms.ModelForm):
    class Meta:
        model = PembelianVoucher
        fields = ['voucher']