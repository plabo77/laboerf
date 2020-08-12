from django.urls import path

from .views import IndexListView

core_patterns = ([
    path('', IndexListView.as_view(), name='home'),
    ], 'core')
