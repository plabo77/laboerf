# Generated by Django 3.0.8 on 2020-07-31 23:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0004_remove_animal_animal_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animalimage',
            options={'ordering': ['created'], 'verbose_name_plural': 'Imagenes por animal'},
        ),
        migrations.AddField(
            model_name='animalimage',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animalimage',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
    ]