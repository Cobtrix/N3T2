from django.urls import path
from . import views

app_name = 'livros'

urlpatterns = [
    path('', views.livros_lista, name='livros_lista'),
    path('livros/novo/', views.livros_criar, name='livros_criar'),
    path('livros/<int:pk>/', views.livros_detalhe, name='livros_detalhe'),
    path('livros/<int:pk>/editar/', views.livros_editar, name='livros_editar'),
    path('livros/<int:pk>/excluir/', views.livros_excluir, name='livros_excluir'),
]