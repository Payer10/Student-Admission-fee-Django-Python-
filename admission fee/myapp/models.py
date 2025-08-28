from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student_Addminssion_fee(models.Model):
    Student_ID = models.PositiveIntegerField(default=0)
    Student_Name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=20,default='email')
    Addmission_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.Student_ID}'