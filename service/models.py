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
    service_type = models.CharField(max_length=60, verbose_name='тип услуги', choices=[('supporting', 'Поддерживающая уборка'), ('full', 'Генеральная уборка'), ('after_renovation', 'Уборка после ремонта')], null=False, default='supporting')
    room_count = models.IntegerField('кол-во комнат', default=1)
    bathroom_count = models.IntegerField(verbose_name='кол-во санузлов', default=1)
    address = models.CharField(max_length= 200, verbose_name='Адрес')
    order_date = models.DateField(verbose_name='Дата заказа')
    date_created = models.DateField(verbose_name='Дата создания заказа', auto_now=True)

    user = models.ForeignKey(User, on_delete= models.CASCADE,verbose_name= 'Клиент', )
     # если нужно сделать поле необязательным, то пропиши дополнительно:
    # blank = True, null = True

    def __str__(self):
        return f'{self.user} {self.order_date} - {self.service_type}'

class Review(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент', null=False, )
    order = models.ForeignKey(Order, verbose_name='Заказ, на который оставлают отзыв', null=False, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True, verbose_name='дата создания отзыва', null=False)
    text = models.TextField()
    scores = models.IntegerField(choices=[(1, '1 звезда'),(2, '2 звезды'),(3, '3 звезды'),(4, '3 звезды'),(5, '5 звезд')], verbose_name='оценка', null=False)

