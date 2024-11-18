# Register your models here.
from django.contrib import admin

from .models import (KategoriJasa, MetodeBayar, Pekerja, PekerjaKategoriJasa,
                     Pelanggan, PesananJasa, SesiLayanan, Subkategori)

admin.site.register(KategoriJasa)
admin.site.register(Subkategori)
admin.site.register(SesiLayanan)
admin.site.register(Pekerja)
admin.site.register(PesananJasa)
admin.site.register(Pelanggan)
admin.site.register(MetodeBayar)
admin.site.register(PekerjaKategoriJasa)

