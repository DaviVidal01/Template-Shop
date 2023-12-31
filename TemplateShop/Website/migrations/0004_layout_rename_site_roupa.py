# Generated by Django 4.2.4 on 2023-08-30 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0003_alter_site_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel', models.ImageField(upload_to='images/')),
                ('icons', models.ImageField(upload_to='images/')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.RenameModel(
            old_name='Site',
            new_name='Roupa',
        ),
    ]
