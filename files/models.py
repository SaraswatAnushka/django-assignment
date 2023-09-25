from django.db import models

class file_Upload(models.Model):
    ids = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    my_files = models.FileField(upload_to='')

# Create your models here.
