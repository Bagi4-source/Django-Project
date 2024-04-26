from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    display_title = models.CharField(max_length=255, verbose_name='Отображаемое название')
    display_on_main_page = models.BooleanField(default=False, verbose_name='Отображение на главной странице')
    file = models.FileField(upload_to='uploads/', verbose_name='Файл')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')


class Tariff(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    cost = models.IntegerField(verbose_name='Стоимость')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.name} {self.cost}'


class Forms(models.Model):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )

    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    registration_address = models.CharField(max_length=255, verbose_name='Адрес регистрации')
    insurance_policy_number = models.CharField(max_length=11, verbose_name='СНИЛС')
    passport_series = models.CharField(max_length=4, verbose_name='Серия паспорта')
    passport_number = models.CharField(max_length=6, verbose_name='Номер паспорта')
    test_type = models.ForeignKey(Tariff, on_delete=models.SET_NULL, null=True, verbose_name='Тип теста')
    trip_number = models.CharField(max_length=100, verbose_name='Номер билета')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'
