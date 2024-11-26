from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import KategoriJasa, Subkategori

def homepage(request):
    kategori_list = KategoriJasa.objects.all()
    return render(request, 'homepage/homepage.html', {'kategori_list': kategori_list})

from django.shortcuts import render

from django.shortcuts import render

def subkategori_detail_user(request):
    # Get subkategori from GET request or session
    subkategori = request.GET.get('subkategori')
    return render(request, 'homepage/subkategori_detail_user.html', {'subkategori': subkategori})


def subkategori_detail_pekerja(request):
    subkategori = request.GET.get('subkategori')
    return render(request, 'homepage/subkategori_detail_pekerja.html', {'subkategori': subkategori})


def view_pemesanan_jasa(request):
    return render(request, 'homepage/view_pemesanan_jasa.html')

def profile_pekerja(request):
    subkategori = request.GET.get('subkategori', 'default_subkategori')  # Get subkategori from query params
    return render(request, 'homepage\profile_pekerja.html', {'subkategori': subkategori})



# def view_pemesanan_jasa(request):
#     pemesanan_jasa = request.GET.get('pemesanan_jasa')
#     return render(request, 'homepage/view_pemesanan_jasa.html', {'pemesanan_jasa': pemesanan_jasa})
# from django.shortcuts import render, redirect
# from .models import Subkategori, SesiLayanan, Pekerja
# from .forms import PesananJasaForm

# def pesan_jasa(request):
#     if request.method == 'POST':
#         form = PesananJasaForm(request.POST)
#         if form.is_valid():
#             pesanan = form.save(commit=False)
#             pesanan.status = 'Menunggu Pembayaran'
#             pesanan.save()
#             return redirect('pesanan_detail', pesanan_id=pesanan.id)
#     else:
#         form = PesananJasaForm()

#     return render(request, 'homepage/pesan_jasa.html', {'form': form})

# from django.shortcuts import render, get_object_or_404
# from .models import PesananJasa

# def pesanan_detail(request, pesanan_id):
#     # Mengambil objek PesananJasa berdasarkan pesanan_id
#     pesanan = get_object_or_404(PesananJasa, pk=pesanan_id)

#     return render(request, 'homepage/pesanan_detail.html', {'pesanan': pesanan})

# from django.contrib.auth.models import Group

# # Membuat group pekerja dan pelanggan
# pekerja_group, created = Group.objects.get_or_create(name='Pekerja')
# pelanggan_group, created = Group.objects.get_or_create(name='Pelanggan')

# from django.shortcuts import render

# # Dummy data for subkategori
# subkategori_data = [
#     {'id': 1, 'nama': 'Daily Cleaning', 'deskripsi': 'Pembersihan harian rumah'},
#     {'id': 2, 'nama': 'Cuci Kasur', 'deskripsi': 'Pembersihan kasur dengan metode khusus'},
#     # Tambahkan data lainnya
# ]

# # Dummy data untuk pekerja
# pekerja_data = [
#     {'id': 1, 'nama': 'John Doe', 'spesialisasi': 'Cleaning'},
#     {'id': 2, 'nama': 'Jane Smith', 'spesialisasi': 'AC Service'},
#     # Tambahkan data lainnya
# ]

# def subkategori_detail_user(request, id):
#     subkategori = next((s for s in subkategori_data if s['id'] == id), None)
#     return render(request, 'subkategori_detail_user.html', {'subkategori': subkategori})

# def subkategori_detail_pekerja(request, id):
#     pekerja = next((p for p in pekerja_data if p['id'] == id), None)
#     return render(request, 'subkategori_detail_pekerja.html', {'pekerja': pekerja})

