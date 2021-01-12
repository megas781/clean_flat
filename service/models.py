from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField()
    initial_price = models.IntegerField()
    add_room_price = models.IntegerField('Цена дополнительной комнаты')
    add_bathroom_price = models.IntegerField('Цена дополнительного санузла')
    date_created = models.DateField(auto_created=True)

    def __str__(self):
        return self.title + ' (' + f'{self.id}' + ')'

class Order(models.Model):
    service_type = models.CharField(max_length=60)
    room_count = models.IntegerField()
    bathroom_count = models.IntegerField()
    address = models.CharField(max_length= 200, verbose_name='')
    order_date = models.DateField(verbose_name='Дата заказа')
    date_created = models.DateField(verbose_name='Дата создания заказа')

    user = models.ForeignKey(User, on_delete= models.CASCADE,verbose_name= 'Клиент')
    # если нужно сделать поле необязательным, то пропиши дополнительно:
    # blank = True, null = True
