from django.urls import path

from .views import IndexView, detail_pet_view, edit_pet_view, new_pet_view

pet_patterns = ([
	path('', IndexView.as_view(), name='index'),
	path('<int:pet_id>/', detail_pet_view, name="detail_pet"),
	path('edit/<int:pet_id>/', edit_pet_view, name="edit_pet"),
	path('new/', new_pet_view, name="new_pet"),
], 'pet')

