from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeesApp.models import Departments, Employees
from EmployeesApp.serializers import DepartmentsSerializers, EmployeesSerializers

# Create your views here.

#Department API defines the CRUD operations of the Departments models
#GET shows all Departments and its columns, POST creates a new department
# #DELETE deletes a department and all its columns from the database, PUT updates information about Departments already stored
@csrf_exempt
def DepartmentsAPI(request,id=0):
    if request.method=="GET":
        department_variable = Departments.objects.all()
        dep_serializer_variable = DepartmentsSerializers(department_variable,many=True)
        return JsonResponse(dep_serializer_variable.data,safe=False)
    elif request.method=="POST":
        dep_data=JSONParser.parse(request)
        dep_serializer_variable=DepartmentsSerializers(data=dep_data)
        if dep_serializer_variable.is_valid():
            dep_serializer_variable.save()
            return JsonResponse("Added Successfully",safe=False)
        else:
            return JsonResponse("Failed to add",safe=False)
    elif request.method=="PUT":
        dep_data=JSONParser.parse(request)
        department_variable=Departments.objects.get(DepartmentID=dep_data["DepartmentID"])
        dep_serializer_variable=DepartmentsSerializers(department_variable,data=dep_data)
        if dep_serializer_variable.is_valid():
            dep_serializer_variable.save()
            return JsonResponse("Updated Successfully",safe=False)
        else:
            return JsonResponse("Failed to Update",safe=False)
    elif request.method=="DELETE":
        department_variable=Departments.objects.get(DepartmentID=id)
        department_variable.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
#Employees API
@csrf_exempt
def EmployeesAPI(request,id=0):