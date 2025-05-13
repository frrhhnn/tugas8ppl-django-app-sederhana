from django.db import models

# Create your models here.

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.IntegerField()
    deskripsi = models.TextField()
    tersedia = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama
