# produk/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produk/', views.daftar_produk, name='daftar_produk'),
    path('produk/<int:id>/', views.detail_produk, name='detail_produk'),
    path('produk/tambah/', views.tambah_produk, name='tambah_produk'),
    path('tentang/', views.tentang, name='tentang'),
]
