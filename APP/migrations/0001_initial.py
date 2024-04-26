# Generated by Django 5.0.4 on 2024-04-26 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('display_title', models.CharField(max_length=255, verbose_name='Отображаемое название')),
                ('display_on_main_page', models.BooleanField(default=False, verbose_name='Отображение на главной странице')),
                ('file', models.FileField(upload_to='uploads/', verbose_name='Файл')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('cost', models.IntegerField(verbose_name='Стоимость')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
        ),
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('gender', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], max_length=1, verbose_name='Пол')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('registration_address', models.CharField(max_length=255, verbose_name='Адрес регистрации')),
                ('insurance_policy_number', models.CharField(max_length=11, verbose_name='СНИЛС')),
                ('passport_series', models.CharField(max_length=4, verbose_name='Серия паспорта')),
                ('passport_number', models.CharField(max_length=6, verbose_name='Номер паспорта')),
                ('trip_number', models.CharField(max_length=100, verbose_name='Номер билета')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('test_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='APP.tariff', verbose_name='Тип теста')),
            ],
        ),
    ]