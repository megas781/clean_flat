from django.db import models

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
