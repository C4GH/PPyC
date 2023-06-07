from django.urls import path
from . import views

urlpatterns = [
    path('combinations/', views.card_combinations_view, name='combinations'),
]
