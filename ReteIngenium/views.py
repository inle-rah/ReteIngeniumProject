from typing import Any, Dict
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q

from ReteIngenium.models import (
    EmployeeInformation,
    ProjectInformation,
    InformationUniteTable,
)


# トップページ
def IndexPage(request):
    return render(request, "index.html")


# エンジニア一覧
class EmployeeList(ListView):
    model = EmployeeInformation
    context_object_name = "employees"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        searchInputText = self.request.GET.get("search")
        if searchInputText:
            context["employees"] = context["employees"].filter(
                Q(familyNameKanji__icontains=searchInputText)
                | Q(firstNameKanji__icontains=searchInputText)
                | Q(familyNameKana__icontains=searchInputText)
                | Q(firstNameKana__icontains=searchInputText)
            )
            context["search"] = searchInputText
        return context


# エンジニア詳細
class EmployeeInfo(DetailView):
    model = EmployeeInformation
    context_object_name = "employeeDetail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from_page = self.request.GET.get("fromPage")
        project_pk = self.request.GET.get("project_pk")
        context["from_page"] = from_page
        context["employeeDetail"] = self.get_object()
        # 案件ページからのアクセス時
        try:
            context["projectDetail"] = ProjectInformation.objects.get(pk=project_pk)
        except ProjectInformation.DoesNotExist:
            context["projectDetail"] = None

        # 紐付け情報存在時
        employee_id = self.object.employeeId
        try:
            context["related_projects"] = InformationUniteTable.get_related_projects(
                employee_id
            )
        except ProjectInformation.DoesNotExist:
            context["related_projects"] = None

        return context


# TODO エンジニア経歴確認画面


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
    model = ProjectInformation
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        searchInputText = self.request.GET.get("search") or None
        if searchInputText:
            context["projects"] = context["projects"].filter(
                Q(projectSummary__icontains=searchInputText)
                | Q(requiredLanguage__icontains=searchInputText)
            )
            context["search"] = searchInputText
        return context


# 案件詳細
class ProjectInfo(DetailView):
    model = ProjectInformation
    context_object_name = "projectDetail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from_page = self.request.GET.get("fromPage")
        employee_pk = self.request.GET.get("employee_pk")
        context["from_page"] = from_page
        # エンジニアページからのアクセス時
        try:
            context["employeeDetail"] = EmployeeInformation.objects.get(pk=employee_pk)
        except EmployeeInformation.DoesNotExist:
            context["employeeDetail"] = None
        # スキルが一致する従業員を取得
        context["employees"] = EmployeeInformation.objects.filter(
            Q(mainLanguage=self.object.requiredLanguage)
            & Q(yearsOfExp__gte=self.object.reqLangExperience)
        )
        context["projectDetail"] = self.get_object()
        return context


# 案件登録
class ProjectRegister(CreateView):
    model = ProjectInformation
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


# 案件受諾（マッチング）
def assign(request, project_id, employee_id):
    project = get_object_or_404(ProjectInformation, projectId=project_id)
    employee = get_object_or_404(EmployeeInformation, employeeId=employee_id)
    if request.method == "POST":
        context = {
            "project": project,
            "employee": employee,
        }
        return render(request, "assign_confirm.html", context)


# アサイン確認画面
def assign_confirm(request, project_id, employee_id):
    if request.method == "POST":
        confirm = request.POST.get("confirm")
        if confirm == "はい":
            if InformationUniteTable.objects.filter(
                empTargetId=employee_id, proTargetId=project_id
            ).exists():
                return render(request, "assign_duplicate.html")
            unite_table = InformationUniteTable(
                empTargetId=employee_id, proTargetId=project_id
            )
            unite_table.save()
            return redirect("index")
        elif confirm == "いいえ":
            # いいえを選択した場合のリダイレクト先を指定
            return redirect("proList")
    return HttpResponseNotAllowed(["POST"])


# 登録情報削除（従業員）
class EmployeeInfoDelete(DeleteView):
    model = EmployeeInformation
    field = "__all__"
    success_url = reverse_lazy("emList")
    context_object_name = "targetemp"


# 登録情報削除（案件）
class ProjectInfoDelete(DeleteView):
    model = ProjectInformation
    field = "__all__"
    success_url = reverse_lazy("proList")
    context_object_name = "targetpro"
