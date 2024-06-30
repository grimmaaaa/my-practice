from django.db import models
from django.contrib.auth.models import AbstractUser

from products.models import Product


class RentPlace(models.Model):

    class PlaceChoices(models.TextChoices):
        hunt = 'ht', 'Охота'
        fishing = 'fh', 'Рыбалка'

    class LocationCountries(models.TextChoices):
        russia = 'ru', 'Россия'
        brasil = 'br', 'Бразилия'
        italy = 'it', 'Италия'
        kenia = 'kn', 'Кения'
        new_zeland = 'nz', 'Новая Зеландия'
        zimbabve = 'zb', 'Зимбабве'

    name = models.CharField('Название', max_length=255)
    location = models.CharField('Локация', choices=LocationCountries, max_length=20)
    inhabiants = models.CharField('Обитатели', max_length=511)
    price = models.PositiveIntegerField('Цена', default=0)
    image = models.ImageField('Картинка', upload_to='images/places')
    place_type = models.CharField('Для охоты или рыбалки', choices=PlaceChoices, max_length=10)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class BaseUser(AbstractUser):
    otchestvo = models.CharField('Отчество', max_length=255)
    have_licence = models.BooleanField('Имеет лицензию', default=False)
    buyed_products = models.ManyToManyField(Product, related_name='users_buy')
    cart = models.ManyToManyField(Product, related_name='users_carted')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class WeaponApplication(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.SET_NULL, null=True)
    weapon_type = models.CharField('Тип оружия', max_length=255)
    reason = models.TextField('Причина получения оружия')
    comment = models.TextField('Комметрарий')
    application_date = models.DateTimeField('Дата подачи заявки', auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.weapon_type}"

    class Meta:
        verbose_name = 'Заяка'
        verbose_name_plural = 'Заявки'
