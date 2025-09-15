from django.db import models

# Create your models here.

#The databases will be created from models, each line of Departments and Employees will be a column of the databases
class Departments(models.Model):
    DepartmentID= models.AutoField(primary_key=True) #ID of the Department
    DepartmentName= models.CharField(max_length=100) #Name of the Department

class Employees(models.Model):
    EmployeeID=models.AutoField(primary_key=True) #ID of the employee
    EmployeeName=models.CharField(max_length=100) #Name of the Employee
    DepartmentName=models.CharField(max_length=100) # Name of the Department the employee works
    DateOfBirth= models.DateField() #Date of Birth of the Employee
    DateOfJoinning=models.DateField() #Date the employee joined the company
    Photo=models.CharField() #field to store the link of the profile picture of the employee