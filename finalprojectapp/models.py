from django.db import models

class courses(models.Model):
    courses_name = models.CharField(max_length=100)
    duresion= models.CharField(max_length=100)
    start_date= models.DateField(max_length=100)
    fee= models.IntegerField()
    timeing=models.CharField(max_length=100)
    trainer_name= models.CharField(max_length=100)
    trainer_exp= models.CharField(max_length=100)

class feedbackData(models.Model):
    content=models.TextField(max_length=1000)
    date=models.DateField(max_length=100)