from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Owner(models.Model):
    full_name = models.CharField('ФИО владельца', max_length=200)
    normalized_phone = PhoneNumberField('Нормализованный номер владельца', region='RU', blank=True, null=True)
    flats = models.ManyToManyField(
        'Flat',
        verbose_name='Квартиры в собственности',
        related_name='owners',
        blank=True,
    )

    def __str__(self):
        return self.full_name


class Flat(models.Model):
    new_building = models.BooleanField('Новостройка:', null=True, blank=True, default=None, db_index=True)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField('Наличие балкона:',null=True, blank=True, default=None)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    likes = models.ManyToManyField(User, related_name='liked_flats', blank=True, verbose_name='Кто лайкнул:')

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'

    def is_liked_by_user(self, user):
        return user in self.likes.all()


class Complaint(models.Model):
    user = models.ForeignKey(User, verbose_name='Кто жаловался', on_delete=models.CASCADE, related_name='complaints')
    flat = models.ForeignKey(
        'Flat',
        verbose_name='Квартира, на которую пожаловались',
        on_delete=models.CASCADE,
        related_name='complaints',
    )
    text = models.TextField('Текст жалобы')

    def __str__(self):
        return f'Жалоба от {self.user} на квартиру {self.flat}'
