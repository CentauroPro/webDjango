# Generated by Django 4.2.4 on 2023-09-07 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='social',
            options={'ordering': ['name'], 'verbose_name': 'Red Social', 'verbose_name_plural': 'Redes Sociales'},
        ),
    ]
