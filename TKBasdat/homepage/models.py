from django.db import models

# Create your models here.
# models.py (dalam aplikasi homepage)
from django.db import models
from django.contrib.auth.models import User

class KategoriJasa(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama

class Subkategori(models.Model):
    kategori = models.ForeignKey(KategoriJasa, related_name='subkategori', on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama
    
class Pelanggan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class SesiLayanan(models.Model):
    subkategori = models.ForeignKey(Subkategori, related_name='sesi_layanan', on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nama} - {self.harga}"
    
    
class MetodeBayar(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama

class Pekerja(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subkategori = models.ForeignKey(Subkategori, related_name='pekerja', on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

class PekerjaKategoriJasa(models.Model):
    pekerja = models.ForeignKey(Pekerja, on_delete=models.CASCADE)
    kategori_jasa = models.ForeignKey(KategoriJasa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pekerja} - {self.kategori_jasa}"

class PesananJasa(models.Model):
    STATUS_CHOICES = [
        ('Menunggu Pembayaran', 'Menunggu Pembayaran'),
        ('Mencari Pekerja Terdekat', 'Mencari Pekerja Terdekat'),
        ('Pesanan Selesai', 'Pesanan Selesai'),
    ]

    subkategori = models.ForeignKey(Subkategori, on_delete=models.CASCADE)
    sesi_layanan = models.ForeignKey(SesiLayanan, on_delete=models.CASCADE)
    pekerja = models.ForeignKey(Pekerja, on_delete=models.CASCADE)
    diskon = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Menunggu Pembayaran')
    tanggal_pemesanan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pesanan {self.subkategori.nama} - {self.sesi_layanan.nama}"