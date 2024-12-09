from django.urls import path

from . import views

urlpatterns = [
    path('testimoni/', views.testimoni_list, name='testimoni_list'),
    path('testimoni/<int:testimoni_id>/', views.testimoni_detail, name='testimoni_detail'),
    path('testimoni/create/<int:pesanan_id>/', views.create_testimoni, name='create_testimoni'),
    path('vouchers/', views.voucher_list, name='voucher_list'),
    path('voucher/<str:kode>/', views.voucher_detail, name='voucher_detail'),
    path('gunakan_voucher/', views.gunakan_voucher, name='gunakan_voucher'),
    path('beli_voucher/<str:kode>/', views.beli_voucher, name='beli_voucher'),
    path('pembelian_voucher/', views.pembelian_voucher_list, name='pembelian_voucher_list'),
]
