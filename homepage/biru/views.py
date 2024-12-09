from django.contrib.auth.decorators import login_required, messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import PembelianVoucherForm, TestimoniForm, VoucherForm
from .models import Pekerja, PembelianVoucher, PesananJasa, Testimoni, Voucher


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
    vouchers = Voucher.objects.all()
    return render(request, 'homepage/voucher_list.html', {'vouchers': vouchers})

def voucher_detail(request, kode):
    voucher = get_object_or_404(Voucher, kode=kode)
    return render(request, 'homepage/voucher_detail.html', {'voucher': voucher})

def gunakan_voucher(request):
    if request.method == 'POST':
        kode = request.POST.get('kode')
        voucher = Voucher.objects.filter(kode=kode).first()
        if voucher and voucher.is_valid():
            messages.success(request, f"Voucher {kode} berhasil digunakan!")
        else:
            messages.error(request, "Voucher tidak valid atau sudah kedaluwarsa.")
    return redirect('voucher_list')

@login_required
def beli_voucher(request, kode):
    voucher = get_object_or_404(Voucher, kode=kode)
    
    # Validasi: Cek apakah voucher sudah kadaluarsa
    if voucher.tanggal_berakhir < timezone.now().date():
        return render(request, 'homepage/error.html', {'message': 'Voucher sudah kadaluarsa'})

    # Validasi: Cek apakah pengguna sudah membeli voucher ini sebelumnya
    pembelian_terdaftar = PembelianVoucher.objects.filter(user=request.user, voucher=voucher).exists()
    if pembelian_terdaftar:
        return render(request, 'homepage/error.html', {'message': 'Anda sudah membeli voucher ini'})

    if request.method == 'POST':
        form = PembelianVoucherForm(request.POST)
        if form.is_valid():
            pembelian = form.save(commit=False)
            pembelian.user = request.user
            pembelian.voucher = voucher
            pembelian.save()
            return redirect('pembelian_voucher_list')
    else:
        form = PembelianVoucherForm()

    return render(request, 'homepage/beli_voucher.html', {'form': form, 'voucher': voucher})