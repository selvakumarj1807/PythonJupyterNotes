from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctor_name=models.CharField(max_length=150)
    department=models.CharField(max_length=150)
    created_at=models.DateTimeField(auto_now_add=True)   
    
    class Meta:
        db_table = "doctor_details"
        
    def __str__(self) :
        return self.doctor_name


class Appoitment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    select_doctor = models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)   
     
    def __str__(self) :
        return self.name + ' - ' + self.select_doctor