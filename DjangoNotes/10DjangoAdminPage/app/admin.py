from django.contrib import admin

# Register your models here.

from .models import *
# Register your models here.


admin.site.register(Doctor)
admin.site.register(Appoitment)