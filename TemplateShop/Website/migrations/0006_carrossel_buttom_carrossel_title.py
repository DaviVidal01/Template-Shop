# Generated by Django 4.2.4 on 2023-09-04 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0005_carrossel_depoimentos_icons_imagens_roupapromo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrossel',
            name='buttom',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='carrossel',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
    ]
