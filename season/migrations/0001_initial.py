# Generated by Django 4.2.4 on 2023-09-07 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(unique=True, verbose_name='Nombre clave')),
                ('name', models.CharField(max_length=50, verbose_name='Temporada')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Acceder')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
            ],
            options={
                'verbose_name': 'Temporada',
                'verbose_name_plural': 'Temporadas',
                'ordering': ['name'],
            },
        ),
    ]