from django.shortcuts import render, redirect, get_object_or_404
from .models import Livros
from .forms import LivrosForm


def livros_lista(request):
    livros = Livros.objects.all().order_by('titulo')
    return render(request, 'livros/livros_lista.html', {'livros':livros})

def livros_criar(request):
    if request.method == 'POST':
        form = LivrosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livros:livros_lista')
    else:
        form = LivrosForm()
        return render(request, 'livros/livros_form.html', {'form': form, 'titulo_pagina': 'Cadastrar Livro'})

def livros_detalhe(request, pk):
    livros = get_object_or_404(Livros, pk=pk)
    return render(request, 'livros/livros_detalhe.html', {'livros': livros})

def livros_editar(request, pk):
    livros = get_object_or_404(Livros, pk=pk)
    if request.method == 'POST':
        form = LivrosForm(request.POST, instance=livros)
        if form.is_valid():
            form.save()
            return redirect('livros:livros_detalhe', pk=livros.pk)
    else:
        form = LivrosForm(instance=livros)
    return render(request, 'livros/livros_form.html', {'form': form, 'livros': livros, 'titulo_pagina': 'Editar Livro'})

def livros_excluir(request, pk):
    livros = get_object_or_404(Livros, pk=pk)
    if request.method == 'POST':
        livros.delete()
        return redirect('livros:livros_lista')
    return render(request, 'livros/livros_confirm_delete.html', {'livros': livros})
