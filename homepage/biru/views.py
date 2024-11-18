from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TestimoniForm, VoucherForm
from .models import Pekerja, PesananJasa, Testimoni, Voucher


@login_required
def create_testimoni(request, pesanan_id):
    pesanan = get_object_or_404(PesananJasa, id=pesanan_id)
    if request.method == 'POST':
        form = TestimoniForm(request.POST)
        if form.is_valid():
            testimoni = form.save(commit=False)
            testimoni.user = request.user
            testimoni.pekerja = pesanan.pekerja
            testimoni.pesanan = pesanan
            testimoni.save()
            return redirect('testimoni_list')
    else:
        form = TestimoniForm()
    return render(request, 'homepage/testimoni_form.html', {'form': form, 'pesanan': pesanan})

def testimoni_list(request):
    testimoni_list = Testimoni.objects.all()
    return render(request, 'homepage/testimoni_list.html', {'testimoni_list': testimoni_list})

def testimoni_detail(request, testimoni_id):
    testimoni = get_object_or_404(Testimoni, id=testimoni_id)
    return render(request, 'homepage/testimoni_detail.html', {'testimoni': testimoni})

def voucher_list(request):
    vouchers = Voucher.objects.filter(aktif=True)
    return render(request, 'homepage/voucher_list.html', {'vouchers': vouchers})

def voucher_detail(request, kode):
    voucher = get_object_or_404(Voucher, kode=kode)
    return render(request, 'homepage/voucher_detail.html', {'voucher': voucher})
