from django.contrib.auth.models import User
from django.db import models


class Testimoni(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pekerja = models.ForeignKey('homepage.Pekerja', on_delete=models.CASCADE)
    pesanan = models.ForeignKey('homepage.PesananJasa', on_delete=models.CASCADE)
    konten = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    tanggal_testimoni = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimoni oleh {self.user.username} - Rating: {self.rating}"

class Voucher(models.Model):
    kode = models.CharField(max_length=20, unique=True)
    deskripsi = models.TextField()
    diskon_persen = models.DecimalField(max_digits=5, decimal_places=2)
    tanggal_mulai = models.DateField()
    tanggal_berakhir = models.DateField()
    jumlah_penggunaan = models.IntegerField(default=0)
    pengguna = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.kode} - {self.diskon_persen}%"
    
    def is_valid(self):
        from datetime import date
        return self.tanggal_mulai <= date.today() <= self.tanggal_berakhir
    
class Voucher(models.Model):
    kode = models.CharField(max_length=50, unique=True)
    deskripsi = models.TextField()
    diskon_persen = models.IntegerField()
    tanggal_mulai = models.DateField()
    tanggal_berakhir = models.DateField()

    def __str__(self):
        return f"{self.kode} - Diskon {self.diskon_persen}%"

class PembelianVoucher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    tanggal_pembelian = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Belum Digunakan', 'Belum Digunakan'), ('Sudah Digunakan', 'Sudah Digunakan')], default='Belum Digunakan')

    def __str__(self):
        return f"{self.user.username} membeli {self.voucher.kode}"