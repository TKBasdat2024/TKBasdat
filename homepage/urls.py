from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('subkategori_detail_user/', views.subkategori_detail_user, name='subkategori_detail_user'),
    path('subkategori_detail_pekerja/', views.subkategori_detail_pekerja, name='subkategori_detail_pekerja'),
    path('pemesanan_jasa/', views.view_pemesanan_jasa, name='view_pemesanan_jasa'),
]
