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
    kode = models.CharField(max_length=50, unique=True)
    deskripsi = models.TextField()
    persentase_diskon = models.DecimalField(max_digits=5, decimal_places=2)
    tanggal_mulai = models.DateField()
    tanggal_berakhir = models.DateField()
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.kode} - {self.persentase_diskon}%"

    def is_valid(self):
        from datetime import date
        return self.aktif and self.tanggal_mulai <= date.today() <= self.tanggal_berakhir