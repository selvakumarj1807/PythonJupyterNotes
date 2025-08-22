from django.contrib import admin

from app.models import Appoitment, Doctor

# Register your models here.
admin.site.register(Doctor)

admin.site.register(Appoitment)