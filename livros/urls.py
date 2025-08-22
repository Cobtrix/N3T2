from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.livros_lista, name='livros_lista'),
    path('livros/novo/', views.contato_criar, name='livros_criar'),
]