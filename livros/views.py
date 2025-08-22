from django.shortcuts import render, redirect
from .models import Contato
from .forms import ContatoForm

def livros_lista(request):

    livros = Livros.objects.all().order_by('titulo')


    return render(request, 'biblioteca/livros_lista.html', {'livros':livros})

def livros_criar(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livros:livros_lista')
    else:
        form = LivrosForm()
    return render(request, 'agenda/livros_form.html', {'form': form, 'titulo_pagina': 'Adicionar Livro'})