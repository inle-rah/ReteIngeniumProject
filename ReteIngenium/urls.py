from django.urls import path
from .views import IndexPage, EmployeeList, EmployeeInfo

urlpatterns = [
    path("", IndexPage, name="index"),
    path("employeelist/", EmployeeList.as_view(), name="emList"),
    path("employeeinfo/<int:pk>", EmployeeInfo.as_view(), name="emInf")
]
