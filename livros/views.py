from django.shortcuts import render
from .models import Livros


def livros_lista(request):

    livros = Livros.objects.all().order_by('titulo')


    return render(request, 'biblioteca/livros_lista.html', {'livros':livros})