from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('sobre',views.sobre,name='sobre'),
path('teste_produto/<int:id>', views.recuperar_produto, name='teste'),
path('listar_produto', views.listar_produtos, name='listar_produtos'),
path('produto/<int:id>', views.detalhar_produto, name='detalhar_produto'),
path('listar_cliente',views.listar_clientes,name='listar_clientes'),
path('cliente/<int:id>',views.detalhar_cliente,name='detalhar_cliente'),
]
