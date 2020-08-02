# Generated by Django 3.0.8 on 2020-07-09 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed_name', models.CharField(max_length=255)),
                ('animal_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.AnimalType')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_name', models.CharField(max_length=255)),
                ('animal_age', models.IntegerField()),
                ('animal_image', models.ImageField(default='media/None/no-img.jpg', upload_to='animal/')),
                ('animal_breed', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='animal.Breed')),
                ('animal_color', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='animal.AnimalColor')),
            ],
        ),
    ]
