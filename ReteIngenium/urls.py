from django.urls import path
from .views import EmployeeList, EmployeeInfo

urlpatterns = [
    path("", EmployeeList.as_view()),
    path("employeeinfo/<int:pk>", EmployeeInfo.as_view(), name="emInf")
]
