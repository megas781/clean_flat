# Generated by Django 3.1.6 on 2021-02-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20210115_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_viewed',
            field=models.BooleanField(default=False, verbose_name='Отзыв просмотрен'),
        ),
    ]