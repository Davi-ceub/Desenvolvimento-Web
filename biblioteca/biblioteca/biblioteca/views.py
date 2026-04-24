from django.shortcuts import render
from .models import Usuario, Autor, Categoria, Livro, Emprestimo


def listar_usuarios(request):
    """Exibe a listagem da tabela `usuarios` (template: `biblioteca/usuarios_list.html`, contexto: `usuarios`)."""
    usuarios = Usuario.objects.all()
    return render(request, 'biblioteca/usuarios_list.html', {'usuarios': usuarios})


def listar_autores(request):
    """Exibe a listagem da tabela `autores` (template: `biblioteca/autores_list.html`, contexto: `autores`)."""
    autores = Autor.objects.all()
    return render(request, 'biblioteca/autores_list.html', {'autores': autores})


def listar_categorias(request):
    """Exibe a listagem da tabela `categorias` (template: `biblioteca/categorias_list.html`, contexto: `categorias`)."""
    categorias = Categoria.objects.all()
    return render(request, 'biblioteca/categorias_list.html', {'categorias': categorias})


def listar_livros(request):
    """Exibe a listagem da tabela `livros` (template: `biblioteca/livros_list.html`, contexto: `livros`)."""
    livros = Livro.objects.all()
    return render(request, 'biblioteca/livros_list.html', {'livros': livros})


def listar_emprestimos(request):
    """Exibe a listagem da tabela `emprestimos` (template: `biblioteca/emprestimos_list.html`, contexto: `emprestimos`)."""
    emprestimos = Emprestimo.objects.all()
    return render(request, 'biblioteca/emprestimos_list.html', {'emprestimos': emprestimos})


def questoes(request):
    return render(request, 'biblioteca/questoes.html' ,{
        'q1': '21',
        'q2': 'Zico Galo',
        'q3': '5',
        'q4': 'bento@vaticano.com',
        'q5': '54',
        'q6': 'Romance',
        'q7': '26',
        'q8': 'Tecendo a Teia',
        'q9': 'email.com',
        'q10': '1899',
    })