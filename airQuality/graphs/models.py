
from django.db import models

# Create your models here.

class FilesUpload(models.Model):
    #No  = models.CharField(max_length=50)
    #Product = models.CharField(max_length=50)
    #Quantity = models.CharField(max_length=50)
    #Salesman= models.CharField(max_length=50)

    date = models.CharField(max_length=50)
    avgPM =models.CharField(max_length=50)

    def __str__(self):
        return f'{self.date} {self.avgPM}'

