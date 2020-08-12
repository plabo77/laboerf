from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .forms import EditPetForm, NewPetForm
from .models import Pet, PetImage


class IndexView(ListView):
    template_name = "pet/index.html"
    model = Pet


def detail_pet_view(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    pet_images = PetImage.objects.filter(pet__id=pet_id)
    return render(request, "pet/detail.html", {'pet': pet, 'pet_images': pet_images})


def edit_pet_view(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    form = EditPetForm(initial={
        'name': pet.name,
        'breed': pet.breed,
        'color': pet.color,
        'age': pet.age
    })
    context = {'form': form, 'pet': pet}
    return render(request, "pet/edit.html", context)


def new_pet_view(request):
    if request.method == "POST":
        form = NewPetForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = NewPetForm()
    return render(request, "pet/edit.html", {'form': form})
