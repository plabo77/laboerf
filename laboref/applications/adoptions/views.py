from django.views.generic import ListView
from applications.animal.models import Animal, AnimalImage


class IndexListView(ListView):
    template_name = "adoptions/adoptions.html"
    model = Animal
    animals = Animal.objects.all()
    animal_images = AnimalImage.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context.update({'animal_list': self.animals, 'animal_images': self.animal_images, })
        return context


"""
class IndexListView(ListView):
    template_name = "core/home.html"
    model = ItemSlider

    items = ItemSlider.objects.all()
    news = News.objects.all()
    first_three_animals = Animal.objects.all().order_by('-created')[:3]

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super(IndexListView, self).get_context_data(**kwargs)
        context.update({'itemslider_list': self.items, 'news_list': self.news, 'animals': self.first_three_animals})
        return context


"""
