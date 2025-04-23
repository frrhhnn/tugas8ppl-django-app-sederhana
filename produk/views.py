from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'produk/home.html')

def daftar_produk(request):
    return render(request, 'produk/daftar_produk.html')

def detail_produk(request, id):
    return render(request, 'produk/detail_produk.html', {'id': id})

def tambah_produk(request):
    return render(request, 'produk/tambah_produk.html')

def tentang(request):
    return render(request, 'produk/tentang.html')