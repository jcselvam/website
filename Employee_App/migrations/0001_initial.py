# Generated by Django 4.1.2 on 2022-10-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpID', models.CharField(max_length=30)),
                ('EmpFName', models.CharField(max_length=100)),
                ('EmpLName', models.CharField(max_length=100)),
                ('EmpEmail', models.EmailField(max_length=100)),
                ('EmpContact', models.CharField(max_length=20)),
                ('EmpAddress', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Employee_App',
            },
        ),
    ]