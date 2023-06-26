from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q

from ReteIngenium.models import (
    EmployeeInformation,
    ProjectInfomation,
    InfomationUniteTable,
)


# トップページ
def IndexPage(request):
    return render(request, "index.html")


# エンジニア一覧
class EmployeeList(ListView):
    model = EmployeeInformation
    context_object_name = "employees"


# エンジニア詳細
class EmployeeInfo(DetailView):
    model = EmployeeInformation
    context_object_name = "employeeDetail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from_page = self.request.GET.get("fromPage")
        context["from_page"] = from_page
        return context


# エンジニア登録
class EmployeeRegister(CreateView):
    model = EmployeeInformation
    fields = [
        "familyNameKanji",
        "firstNameKanji",
        "familyNameKana",
        "firstNameKana",
        "employeeAge",
        "employeeSex",
        "employeeArea",
        "certification",
        "mainLanguage",
        "yearsOfExp",
    ]
    success_url = reverse_lazy("emList")


# 案件一覧
class ProjectList(ListView):
    model = ProjectInfomation
    context_object_name = "projects"


# 案件詳細
class ProjectInfo(DetailView):
    model = ProjectInfomation
    context_object_name = "projectDetail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # スキルが一致する従業員を取得
        context["employees"] = EmployeeInformation.objects.filter(
            Q(mainLanguage=self.object.requiredLanguage)
            & Q(yearsOfExp__gte=self.object.reqLangExperience)
        )
        context["projectDetail"] = self.get_object()
        return context


# 案件登録
class ProjectRegister(CreateView):
    model = ProjectInfomation
    fields = [
        "projectSummary",
        "projectCliant",
        "projectUnitPrice",
        "workPlace",
        "requiredLanguage",
        "reqLangExperience",
        "projectDevEnv",
        "projectDetail",
    ]
    success_url = reverse_lazy("proList")


# TODO 案件受諾（マッチング）
def EmployeeMatching(request, *targetproject, **candidateemployee):
    pass
    return
