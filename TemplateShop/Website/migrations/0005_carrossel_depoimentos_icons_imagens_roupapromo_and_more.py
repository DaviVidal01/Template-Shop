# Generated by Django 4.2.4 on 2023-08-31 01:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0004_layout_rename_site_roupa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrossel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrossel', models.ImageField(upload_to='images/')),
                ('description', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Depoimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('depoimento', models.TextField(max_length=255)),
                ('date_create', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icones', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagens', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='RoupaPromo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=255)),
                ('path', models.ImageField(upload_to='images/')),
                ('preco_produto', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('desconto', models.IntegerField(default=0)),
                ('usuario', models.CharField(max_length=20)),
                ('date_create', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='RoupaSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=255)),
                ('path', models.ImageField(upload_to='images/')),
                ('preco_produto', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('usuario', models.CharField(max_length=20)),
                ('date_create', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.TextField(max_length=255)),
                ('lembrar', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameModel(
            old_name='Roupa',
            new_name='RoupaCasual',
        ),
        migrations.DeleteModel(
            name='Layout',
        ),
    ]