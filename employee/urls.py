from . import views
from django.urls import path

urlpatterns = [
    path('employeeList/', views.employeeList,name="employeeList"),
    path('update/<int:id>/', views.updateEmployee, name="updateEmployee"),
    path('delete/<int:id>/', views.deleteEmployee, name="deleteEmployee"),
    path('sort/', views.sortEmployee, name="sortEmployee"),
     path('dsort/', views.dsortEmployee, name="dsortEmployee"),
    path('createEmployee/',views.createEmployee,name="createEmployee")
]