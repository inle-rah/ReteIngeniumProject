from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from ReteIngenium.models import EmployeeInformation

# Create your views here.
class EmployeeList(ListView):
    model = EmployeeInformation
    context_object_name = "employees"
    
class EmployeeInfo(DetailView):
    model = EmployeeInformation
    context_object_name = "employeeDetail"
    