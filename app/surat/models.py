from django.db import models

class surat_masuk(models.Model):
    asal_surat = models.CharField(max_length=100)
    kode = models.CharField(max_length=30)
    perihal = models.CharField(max_length=150)
    tgl_surat = models.DateTimeField()
    tgl_terima = models.DateTimeField()
    file = models.FileField(upload_to='documents/')
    keterangan = models.CharField(max_length=225)
