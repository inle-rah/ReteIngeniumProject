from django.urls import path
from .views import EmployeeList, EmployeeInfo

urlpatterns = [
    # path("", IndexView.as_view()),
    path("", EmployeeList.as_view(), name="emList"),
    path("employeeinfo/<int:pk>", EmployeeInfo.as_view(), name="emInf")
]
