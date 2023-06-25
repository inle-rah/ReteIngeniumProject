from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from ReteIngenium.models import EmployeeInformation, ProjectInfomation

# トップページ
def IndexPage(request):
    return render(request, 'index.html')

# エンジニア一覧
class EmployeeList(ListView):
    model = EmployeeInformation
    context_object_name = "employees"

# エンジニア詳細
class EmployeeInfo(DetailView):
    model = EmployeeInformation
    context_object_name = "employeeDetail"
    
# TODO 案件一覧

# TODO 案件詳細

# TODO 案件受諾（マッチング）