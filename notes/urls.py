from django.urls import path
from .views import note_list, note_create

urlpatterns = [
    path('', note_list, name='note_list'),
    path('create/', note_create, name='note_create'),
]
