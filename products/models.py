from django.db import models


class Product(models.Model):

    class ColorChoices(models.TextChoices):
        red = 'red', 'Красный'
        green = 'green', 'Зелёный'
        blue = 'blue', 'Синий'
        yellow = 'yellow', 'Жёлтый'
        black = 'black', 'Чёрный'

    name = models.CharField('Имя', max_length=255)
    price = models.PositiveIntegerField('Цена', default=0)
    desc = models.TextField('Описание')
    color = models.CharField('Цвет', max_length=255, choices=ColorChoices)
    producer_country = models.CharField('Старана производитель', max_length=255)
    image = models.ImageField('Картинка', upload_to='images/')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    user = models.ForeignKey('main.BaseUser', on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(Product, related_name='orders')
    datetime_made = models.DateTimeField('Время заказа', auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class RentOrder(models.Model):
    user = models.ForeignKey('main.BaseUser', on_delete=models.SET_NULL, null=True)
    place = models.ForeignKey('main.RentPlace', on_delete=models.SET_NULL, null=True)
    datetime_made = models.DateTimeField('Время заказа', auto_now=True)

    class Meta:
        verbose_name = 'Заказ оренды'
        verbose_name_plural = 'Заказы оренды'
