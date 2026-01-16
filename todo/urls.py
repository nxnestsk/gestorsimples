from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('editar/<int:tarefa_id>/', views.editar_tarefa, name='editar_tarefa'),
    path('concluir/<int:tarefa_id>/', views.marcar_concluida, name='marcar_concluida'),
    path('remover/<int:tarefa_id>/', views.remover_tarefa, name='remover_tarefa'),
    path('categoria/adicionar/', views.adicionar_categoria, name='adicionar_categoria'),
    path('categoria/remover/<int:categoria_id>/', views.remover_categoria, name='remover_categoria'),
]