# Generated by Django 3.0.8 on 2020-07-14 03:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Nombre Del Colaborador')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, null=True, upload_to='collaborator')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Colaborador',
                'verbose_name_plural': 'Colaboradores',
                'ordering': ['created'],
            },
        ),
    ]
