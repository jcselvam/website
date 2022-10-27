from django.db import models

class Employee(models.Model):
    EmpID = models.CharField(max_length=30)
    EmpFName = models.CharField(max_length=100)
    EmpLName = models.CharField(max_length=100)
    EmpEmail = models.EmailField(max_length=100)   
    EmpContact = models.CharField(max_length=20)
    EmpAddress = models.CharField(max_length=200)

    class Meta:
        db_table = 'Employee_App'