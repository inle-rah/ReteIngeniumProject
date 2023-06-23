# Generated by Django 4.2.2 on 2023-06-23 07:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeId', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('familyNameKanji', models.CharField(max_length=10)),
                ('firstNameKanji', models.CharField(max_length=10)),
                ('familyNameKana', models.CharField(max_length=15)),
                ('firstNameKana', models.CharField(max_length=15)),
                ('employeeAge', models.IntegerField()),
                ('employeeSex', models.CharField(max_length=10)),
                ('employeeArea', models.CharField(max_length=15)),
                ('certification', models.TextField(max_length=100)),
                ('mainLanguage', models.CharField(max_length=10)),
                ('yearsOfExp', models.IntegerField()),
                ('careerList', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
            options={
                'ordering': ['yearsOfExp'],
            },
        ),
        migrations.CreateModel(
            name='ProjectInfomation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectId', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('projectSummary', models.CharField(max_length=50)),
                ('projectRegisteredDate', models.DateField(auto_now_add=True)),
                ('projectCliant', models.CharField(max_length=15)),
                ('projectUnitPrice', models.IntegerField()),
                ('workPlace', models.CharField(max_length=15)),
                ('requiredLanguage', models.CharField(max_length=10)),
                ('reqLangExperience', models.IntegerField()),
                ('projectDevEnv', models.TextField(max_length=100)),
                ('projectDetail', models.TextField(max_length=500)),
            ],
            options={
                'ordering': ['projectRegisteredDate'],
            },
        ),
    ]
