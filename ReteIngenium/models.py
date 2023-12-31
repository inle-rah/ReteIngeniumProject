import uuid
from django.db import models
from django.contrib.auth.models import User


# 従業員情報
class EmployeeInformation(models.Model):
    # 従業員ID
    employeeId = models.UUIDField(default=uuid.uuid4, editable=False)
    # 姓/名(漢字/フリガナ)
    familyNameKanji = models.CharField(max_length=10)
    firstNameKanji = models.CharField(max_length=10)
    familyNameKana = models.CharField(max_length=15)
    firstNameKana = models.CharField(max_length=15)
    # 年齢
    employeeAge = models.IntegerField()
    # 性別
    employeeSex = models.CharField(max_length=10)
    # 最寄駅
    employeeArea = models.CharField(max_length=15)
    # 所有資格
    certification = models.TextField(max_length=100)
    # メイン言語
    mainLanguage = models.CharField(max_length=10)
    # メイン言語の経験年数
    yearsOfExp = models.IntegerField()

    def __str__(self):
        return self.familyNameKanji

    class Meta:
        ordering = ["yearsOfExp"]


# 案件情報
class ProjectInformation(models.Model):
    # 案件識別ID
    projectId = models.UUIDField(default=uuid.uuid4, editable=False)
    # 案件概要
    projectSummary = models.CharField(max_length=50)
    # 案件登録日
    projectRegisteredDate = models.DateField(auto_now_add=True)
    # 依頼企業名
    projectCliant = models.CharField(max_length=15)
    # 単価(中央値)
    projectUnitPrice = models.IntegerField()
    # 勤務地
    workPlace = models.CharField(max_length=15)
    # 必須スキル（言語）
    requiredLanguage = models.CharField(max_length=10)
    # 上記の経験年数
    reqLangExperience = models.IntegerField()
    # 開発環境
    projectDevEnv = models.TextField(max_length=100)
    # 案件詳細
    projectDetail = models.TextField(max_length=500)

    def __str__(self):
        return self.workPlace

    class Meta:
        ordering = ["projectRegisteredDate"]


# 登録情報紐付けテーブル
class InformationUniteTable(models.Model):
    # 従業員側targetId
    empTargetId = models.UUIDField()
    # 案件側targetId
    proTargetId = models.UUIDField()
    # 登録日
    projectRegisteredDate = models.DateField(auto_now_add=True)

    # 　従業員のIDを受け取り、紐づけしたデータを返却
    def get_related_projects(emp_target_id):
        pro_target_ids = InformationUniteTable.objects.filter(
            empTargetId=emp_target_id
        ).values_list("proTargetId")
        return ProjectInformation.objects.filter(projectId__in=pro_target_ids)
