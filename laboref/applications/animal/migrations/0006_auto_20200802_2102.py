# Generated by Django 3.0.8 on 2020-08-02 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0005_auto_20200731_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalimage',
            name='main',
            field=models.BooleanField(default=False, verbose_name='Principal'),
        ),
        migrations.AlterField(
            model_name='animalimage',
            name='image_animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Animal', verbose_name='Imagen de animal'),
        ),
        migrations.AlterField(
            model_name='animalimage',
            name='image_description',
            field=models.TextField(verbose_name='Descripción de la imagen'),
        ),
        migrations.AlterField(
            model_name='animalimage',
            name='image_url',
            field=models.ImageField(default='media/None/no-img.jpg', upload_to='animal/', verbose_name='Url par imagen'),
        ),
    ]
