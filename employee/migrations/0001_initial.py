# Generated by Django 3.1.7 on 2021-04-09 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('ProjectId', models.AutoField(primary_key=True, serialize=False)),
                ('ProjectNm', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('RoleId', models.AutoField(primary_key=True, serialize=False)),
                ('RoleNm', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_id', models.IntegerField(blank=True)),
                ('emp_name', models.CharField(max_length=255)),
                ('date_time_in', models.CharField(max_length=255)),
                ('date_time_out', models.CharField(max_length=255)),
                ('duration', models.FloatField()),
                ('is_approved', models.BooleanField(default=False)),
                ('ProjectId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.project')),
                ('RoleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.roles')),
            ],
        ),
    ]
