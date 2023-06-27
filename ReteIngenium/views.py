from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
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
        project_pk = self.request.GET.get("project_pk")
        context["from_page"] = from_page
        # 案件ページ以外から飛ぶ際はExceptが発生→空で送って処理
        try:
            context["projectDetail"] = ProjectInfomation.objects.get(pk=project_pk)
        except ProjectInfomation.DoesNotExist:
            context["projectDetail"] = None
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


# 案件受諾（マッチング）
def assign(request, project_id, employee_id):
    project = get_object_or_404(ProjectInfomation, projectId=project_id)
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
            # 重複レコードがある場合削除
            InfomationUniteTable.objects.filter(
                empTargetId=employee_id, proTargetId=project_id
            ).delete()
            unite_table = InfomationUniteTable(
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
    model = ProjectInfomation
    field = "__all__"
    success_url = reverse_lazy("proList")
    context_object_name = "targetpro"
