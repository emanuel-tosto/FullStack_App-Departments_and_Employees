from EmployeesApp import views
from django.urls import path

urlpatterns=[
    path("department/",views.DepartmentsAPI),
    path("department/([0-9]+)")

    path("employee/", views.EmployeesAPI),
    path("employee/([0-9]+)")

    path("SaveFile",views.SaveFile)

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)