from django.db import models

# Create your models here.

class PersonData(models.Model) :
    Name = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Title = models.CharField(max_length=100) 
    Branch = models.CharField(max_length=50)
    Assessment_Date = models.DateTimeField(auto_now_add=True)
    Evaluation_Date = models.DateTimeField(auto_now_add=True)
    Expiration_Date = models.DateTimeField(auto_now_add=True)
    Teaching_Level = models.CharField(max_length=20)
    Document_Level = models.CharField(max_length=20)
    Rating_Time = models.IntegerField()

class Status(models.Model) :
    Number = models.IntegerField()
    Name = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Request_Date = models.DateTimeField(auto_now_add=True)
    Date_Board_Resolution = models.DateTimeField(auto_now_add=True)
    Evaluation_Date = models.DateTimeField(auto_now_add=True)
    Due_Date = models.DateTimeField(auto_now_add=True)
    Position_On_The_Request = models.CharField(max_length=100)
    Execution_Status = models.CharField(max_length=100) 