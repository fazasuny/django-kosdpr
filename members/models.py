from django.db import models

class anggota(models.Model):
  name = models.CharField(max_length=255)
  penjuruan = models.CharField(max_length=255)
  asal = models.CharField(max_length=255)

  
  
  def __str__(self):
    return f"{self.name}"