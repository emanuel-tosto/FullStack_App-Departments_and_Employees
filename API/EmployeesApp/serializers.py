from rest_framework import serializers
from EmployeesApp.models import Departments, Employees

class DepartmentsSerializers(serializers.ModelSerializer):
    class Meta:
        model= Departments
        fields= ("DepartmentID","DepartmentName")

class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        model= Employees
        fields= ("EmployeeID",
                 "EmployeeName",
                 "DepartmentName",
                 "DateOfBirth",
                 "DateOfJoining",
                 "Photo")