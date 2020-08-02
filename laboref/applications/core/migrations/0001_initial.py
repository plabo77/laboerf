# Generated by Django 3.0.8 on 2020-07-14 18:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Titulo')),
                ('description', models.TextField(max_length=50, verbose_name='Descripcion')),
                ('image', models.ImageField(blank=True, null=True, upload_to='itemsSlider')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
            ],
            options={
                'verbose_name': 'Item deslizador',
                'verbose_name_plural': 'Items del deslizador',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Titulo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Título')),
                ('image', models.ImageField(blank=True, null=True, upload_to='welcome')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Bienvenida',
                'verbose_name_plural': 'Bienvenidas',
                'ordering': ['created'],
            },
        ),
    ]