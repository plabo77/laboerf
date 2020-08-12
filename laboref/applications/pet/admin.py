from django.contrib import admin
from .models import PetType, Breed, PetColor, Pet, PetImage

admin.site.register(Pet)
admin.site.register(PetType)
admin.site.register(Breed)
admin.site.register(PetColor)
admin.site.register(PetImage)
