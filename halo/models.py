from django.db import models

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    stok = models.IntegerField()
    harga = models.IntegerField()

    def __str__(self):
        return self.nama