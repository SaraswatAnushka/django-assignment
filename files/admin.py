from django.contrib import admin

from .models import file_Upload



# Register your models here.
admin.site.register(file_Upload)

def __str__(self):
    return self.file_name
