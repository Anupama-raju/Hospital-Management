from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=255)
    dep_description=models.TextField()
    
    def __str__(self):    
        return self.dep_name
    
class Doctors(models.Model):
    d_name=models.CharField(max_length=255)
    speciality=models.CharField(max_length=255)
    dep_name=models.ForeignKey(Department, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='hos_images')
    
    def __str__(self):
        return 'Dr ' + self.d_name + '-(' + self.speciality + ')'
    
class Booking(models.Model):
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    d_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True) 
    
# class Register(models.Model):
#     fname=models.CharField(max_length=255)
#     lname=models.CharField(max_length=255)
#     email=models.EmailField()
#     username=models.CharField()
#     password=models.CharField()
  
