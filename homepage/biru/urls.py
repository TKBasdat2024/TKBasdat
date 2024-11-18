from django.urls import path

from . import views

urlpatterns = [
    path('testimoni/', views.testimoni_list, name='testimoni_list'),
    path('testimoni/<int:testimoni_id>/', views.testimoni_detail, name='testimoni_detail'),
    path('testimoni/create/<int:pesanan_id>/', views.create_testimoni, name='create_testimoni'),
    path('vouchers/', views.voucher_list, name='voucher_list'),
    path('vouchers/<str:kode>/', views.voucher_detail, name='voucher_detail'),
]
