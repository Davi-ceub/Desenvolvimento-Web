from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name='biblioteca/inicio.html'),
        name='inicio',
    ),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('autores/', views.listar_autores, name='listar_autores'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('livros/', views.listar_livros, name='listar_livros'),
    path('emprestimos/', views.listar_emprestimos, name='listar_emprestimos'),
    path('questoes/', views.questoes, name='questoes'),
]
