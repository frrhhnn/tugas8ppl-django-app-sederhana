from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produk

# Create your views here.
def home(request):
    # Get 3 latest products for the homepage
    latest_products = Produk.objects.all().order_by('-created_at')[:3]
    return render(request, 'produk/home.html', {'latest_products': latest_products})

def daftar_produk(request):
    # Get all products ordered by creation date
    products = Produk.objects.all().order_by('-created_at')
    return render(request, 'produk/daftar_produk.html', {'produk_list': products})

def detail_produk(request, id):
    # Get product by ID or return 404
    produk = get_object_or_404(Produk, id=id)
    return render(request, 'produk/detail_produk.html', {'produk': produk})

def tambah_produk(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        harga = request.POST.get('harga')
        deskripsi = request.POST.get('deskripsi')
        tersedia = request.POST.get('tersedia') == 'on'
        
        # Validate required fields
        if not nama or not harga:
            messages.error(request, 'Nama dan harga wajib diisi!')
            return render(request, 'produk/tambah_produk.html', {
                'nama': nama,
                'harga': harga,
                'deskripsi': deskripsi,
                'tersedia': tersedia
            })
        
        try:
            # Create new product
            Produk.objects.create(
                nama=nama,
                harga=harga,
                deskripsi=deskripsi,
                tersedia=tersedia
            )
            messages.success(request, 'Produk berhasil ditambahkan!')
            return redirect('daftar_produk')
        except Exception as e:
            messages.error(request, f'Terjadi kesalahan: {str(e)}')
            return render(request, 'produk/tambah_produk.html', {
                'nama': nama,
                'harga': harga,
                'deskripsi': deskripsi,
                'tersedia': tersedia
            })
    
    return render(request, 'produk/tambah_produk.html')

def edit_produk(request, id):
    produk = get_object_or_404(Produk, id=id)
    
    if request.method == 'POST':
        nama = request.POST.get('nama')
        harga = request.POST.get('harga')
        deskripsi = request.POST.get('deskripsi')
        tersedia = request.POST.get('tersedia') == 'on'
        
        if not nama or not harga:
            messages.error(request, 'Nama dan harga wajib diisi!')
            return render(request, 'produk/edit_produk.html', {'produk': produk})
        
        try:
            # Update product
            produk.nama = nama
            produk.harga = harga
            produk.deskripsi = deskripsi
            produk.tersedia = tersedia
            produk.save()
            
            messages.success(request, 'Produk berhasil diupdate!')
            return redirect('detail_produk', id=produk.id)
        except Exception as e:
            messages.error(request, f'Terjadi kesalahan: {str(e)}')
            return render(request, 'produk/edit_produk.html', {'produk': produk})
    
    return render(request, 'produk/edit_produk.html', {'produk': produk})

def hapus_produk(request, id):
    produk = get_object_or_404(Produk, id=id)
    try:
        produk.delete()
        messages.success(request, 'Produk berhasil dihapus!')
    except Exception as e:
        messages.error(request, f'Terjadi kesalahan: {str(e)}')
    return redirect('daftar_produk')

def tentang(request):
    return render(request, 'produk/tentang.html')