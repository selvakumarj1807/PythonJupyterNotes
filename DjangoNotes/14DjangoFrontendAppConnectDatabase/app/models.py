from django.db import models

from datetime import datetime
import os

def getFileName(request, filename):
    now_time = datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = f"{now_time}_{filename}" 
    return os.path.join('doctorIMG', new_filename)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, default='Dentist')
    description = models.TextField()
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")

    def __str__(self):
        return self.name