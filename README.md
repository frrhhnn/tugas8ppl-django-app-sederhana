# Toko Kita - Sistem Manajemen Produk

Toko Kita adalah aplikasi web manajemen produk yang dibangun dengan Django dan Tailwind CSS. Aplikasi ini menyediakan antarmuka yang modern dan intuitif untuk mengelola katalog produk.

## Fitur Utama

- **Manajemen Produk Lengkap**
  - Tambah, edit, dan hapus produk
  - Form input yang intuitif dengan validasi
  - Status ketersediaan produk
  - Informasi detail produk terstruktur

- **Katalog Interaktif**
  - Tampilan produk yang responsif
  - Fitur pencarian dan filter
  - Tata letak yang bersih dan modern
  - Animasi dan efek transisi yang halus

- **Antarmuka Modern**
  - Desain minimalis dan profesional
  - Gradien warna yang menarik
  - Komponen yang konsisten
  - Responsif di semua ukuran layar

## Teknologi

- **Django** - Framework Python untuk pengembangan web
- **Tailwind CSS** - Framework CSS utility-first
- **SQLite** - Database ringan untuk penyimpanan data
- **Bootstrap Icons** - Library ikon yang lengkap

## Struktur Template

```
produk/templates/produk/
├── base.html          # Template dasar dengan layout umum
├── home.html          # Halaman beranda
├── daftar_produk.html # Daftar/katalog produk
├── detail_produk.html # Detail produk individual
├── tambah_produk.html # Form tambah produk baru
├── edit_produk.html   # Form edit produk
└── tentang.html       # Halaman informasi aplikasi
```

## Instalasi

1. Clone repository
```bash
git clone [repository-url]
```

2. Buat virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Jalankan migrasi database
```bash
python manage.py migrate
```

5. Jalankan server development
```bash
python manage.py runserver
```

## Pengembangan

- Template menggunakan Tailwind CSS untuk styling
- Komponen UI dibuat dengan pendekatan mobile-first
- Menggunakan class utility Tailwind untuk konsistensi
- Animasi dan transisi untuk UX yang lebih baik

## Kontribusi

Silakan berkontribusi dengan membuat pull request. Untuk perubahan besar, harap buka issue terlebih dahulu untuk mendiskusikan perubahan yang diinginkan.

