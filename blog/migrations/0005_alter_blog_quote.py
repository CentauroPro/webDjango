# Generated by Django 4.2.4 on 2023-09-08 22:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='quote',
            field=ckeditor.fields.RichTextField(default='“There are always two people in every picture: the photographer and the viewer.” - Ansel Adams', verbose_name='Cita'),
        ),
    ]