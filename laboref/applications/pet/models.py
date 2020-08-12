from django.db import models
from ckeditor.fields import RichTextField


# tipo de pet
class PetType(models.Model):
    pet_type_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tipo de las mascota"
        verbose_name_plural = "Tipos de las mascotas"

    def __str__(self):
        return self.pet_type_name


# raza
class Breed(models.Model):
    pet_type = models.ForeignKey(PetType, on_delete=models.CASCADE)
    breed_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Raza de la mascota"
        verbose_name_plural = "Razas"

    def __str__(self):
        return self.breed_name


# color de la mascota
class PetColor(models.Model):
    color_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Color de la mascota"
        verbose_name_plural = "Color de las mascotas"

    def __str__(self):
        return self.color_name


# pet
class Pet(models.Model):
    name = models.CharField(max_length=255)
    breed = models.ForeignKey(Breed, on_delete=models.DO_NOTHING)
    color = models.ForeignKey(PetColor, on_delete=models.DO_NOTHING)
    age = models.IntegerField()
    description = RichTextField(verbose_name="Descripción")
    avatar = models.ImageField(upload_to='pet/', default='None/no_img.png')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name_plural = "Mascotas"
        ordering = ['created']

    def __str__(self):
        return self.name


# pets images
class PetImage(models.Model):
    description = models.TextField(verbose_name="Descripción de la imagen")
    url = models.ImageField(upload_to='pets/', default='media/None/no-img.jpg', verbose_name="Url par imagen")
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, verbose_name="Imagen de la mascota")
    main = models.BooleanField(default=False, verbose_name="Principal")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name_plural = "Imagenes por mascota"
        ordering = ['created']

    def __str__(self):
        return self.description
