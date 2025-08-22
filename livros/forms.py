from django import forms
from .models import Livros # Importe o modelo Contato

class LivrosForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ['titulo', 'autor', 'ano_publicacao', 'sinopse']

