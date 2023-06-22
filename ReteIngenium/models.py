import uuid
from django.db import models
from django.contrib.auth.models import User
from datetime import timezone

# 従業員情報
class EmployeeInformation(models.Model):
    # 従業員ID(uuidで複雑化)
    employeeId = models.UUIDField(default=uuid.uuid4, editable=False)
    # 姓/名(漢字/フリガナ/ローマ字)
    familyNameKanji = models.CharField(max_length=10)
    firstNameKanji = models.CharField(max_length=10)
    familyNameKana = models.CharField(max_length=10)
    firstNameKana = models.CharField(max_length=10)
    familyNameEiji = models.CharField(max_length=10, null=True)
    firstNameEiji = models.CharField(max_length=10, null=True)
    # 性別(1:男/2:女/3:その他)
    employeeSex = models.IntegerField()
    # 年齢
    employeeAge = models.IntegerField()
    # 住所(最寄り駅)
    employeeArea = models.CharField(max_length=15)
    # 所有資格(従業員IDを流用し、他テーブルとの結合)
    certificationList = models.UUIDField(default=uuid.uuid4, editable=False)
    # 実務経験年数
    totalYearOfExperience = models.IntegerField()
    # 経歴(結合用ID)
    careerId = models.UUIDField(default=uuid.uuid4, editable=False)
    # アサイン可能かどうか
    assignCheckFlg = models.BooleanField(default=False)
    
    def __str__(self):
        return self.familyNameKanji
    
    class Meta:
        ordering = ["totalYearOfExperience"]

# 案件情報
class ProjectInfomation(models.Model):
    # 案件識別ID
    projectId = models.UUIDField(default=uuid.uuid4, editable=False)
    # 企業名（正式名称）
    companyName = models.CharField(max_length=50)
    # 案件概要
    projectSummary = models.CharField(max_length=50)
    # 案件登録日
    projectAcceptedDate = models.DateField(auto_now_add=True)
    # 単価(min~max)
    unitPriceMin = models.IntegerField()
    unitPriceMax = models.IntegerField()
    # 勤務地
    workPlace = models.CharField(max_length=15)
    # 予定業務期間(自)/(至)
    workPeriodStart = models.DateField(default=timezone.now)
    workPeriodfinish = models.DateField(default=timezone.now)