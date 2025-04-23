
# Toko - A Simple Django-Based E-Commerce App

This project is a basic e-commerce web application built using the Django framework. It provides functionality to display, add, and manage products. This can serve as a starter template for building more complex Django applications.

## 📁 Project Structure

```
Toko/
├── db.sqlite3               # SQLite database file
├── manage.py                # Django management script
├── produk/                  # Main app handling product features
│   ├── admin.py             # Admin interface configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models for products
│   ├── tests.py             # Test cases for the app
│   ├── urls.py              # URL routing for 'produk' app
│   ├── views.py             # Views (controllers) for handling logic
│   ├── migrations/          # Database migration files
│   └── templates/           # HTML templates
│       └── produk/
│           ├── base.html
│           ├── daftar_produk.html
│           ├── detail_produk.html
│           ├── home.html
│           ├── tambah_produk.html
│           └── tentang.html
└── Toko/                    # Main project settings
    ├── asgi.py
    ├── settings.py          # Project settings
    ├── urls.py              # Project-wide URL configuration
    ├── wsgi.py
```

## ⚙️ Features

- View a list of products
- View product details
- Add new products
- Simple navigation pages (home, about)
- Admin panel to manage data

## 🚀 Getting Started

1. **Clone the repository**

```bash
git clone https://github.com/your-username/toko.git
cd toko
```

2. **Set up a virtual environment and install dependencies**

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install django
```

3. **Run migrations and start the server**

```bash
python manage.py migrate
python manage.py runserver
```

4. **Access the app**

Open your browser and navigate to `http://127.0.0.1:8000/`

## 🧑‍💻 Author

- Farhanul Khair - 2208107010076
- Ganang Setyo Hadi - 2208107010052
- Alfi Zamriza - 2208107010080
---

Feel free to fork or contribute to this project!
