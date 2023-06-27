from django.urls import path
from .views import (
    IndexPage,
    EmployeeList,
    EmployeeInfo,
    EmployeeRegister,
    EmployeeInfoDelete,
    ProjectList,
    ProjectInfo,
    ProjectRegister,
    ProjectInfoDelete,
    assign,
    assign_confirm,
)

urlpatterns = [
    path("", IndexPage, name="index"),
    path("employee-list/", EmployeeList.as_view(), name="emList"),
    path("employee-info/<int:pk>", EmployeeInfo.as_view(), name="emInfo"),
    path("employee-register/", EmployeeRegister.as_view(), name="emReg"),
    path("employee-delete/<int:pk>", EmployeeInfoDelete.as_view(), name="emDel"),
    path("project-list/", ProjectList.as_view(), name="proList"),
    path("project-info/<int:pk>", ProjectInfo.as_view(), name="proInfo"),
    path("project-register/", ProjectRegister.as_view(), name="proReg"),
    path("project-delete/<int:pk>", ProjectInfoDelete.as_view(), name="proDel"),
    path("assign/<uuid:project_id>/<uuid:employee_id>/", assign, name="assign"),
    path(
        "assign-confirm/<uuid:project_id>/<uuid:employee_id>/",
        assign_confirm,
        name="assign_confirm",
    ),
]
