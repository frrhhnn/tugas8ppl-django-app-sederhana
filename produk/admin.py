from django.contrib import admin
from .models import Produk

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ['nama', 'harga', 'tersedia', 'created_at']
    list_filter = ['tersedia']
    search_fields = ['nama']
