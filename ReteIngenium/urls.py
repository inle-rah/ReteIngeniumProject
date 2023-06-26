from django.urls import path
from .views import (
    IndexPage,
    EmployeeList,
    EmployeeInfo,
    EmployeeRegister,
    ProjectList,
    ProjectInfo,
    ProjectRegister,
)

urlpatterns = [
    path("", IndexPage, name="index"),
    path("employee-list/", EmployeeList.as_view(), name="emList"),
    path("employee-info/<int:pk>", EmployeeInfo.as_view(), name="emInfo"),
    path("employee-register/", EmployeeRegister.as_view(), name="emReg"),
    path("project-list/", ProjectList.as_view(), name="proList"),
    path("project-info/<int:pk>", ProjectInfo.as_view(), name="proInfo"),
    path("project-register/", ProjectRegister.as_view(), name="proReg"),
]
