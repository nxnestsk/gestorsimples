from django.urls import path
from . import views 

urlpatterns = [
   
    path('', views.lista_tarefas, name='lista_tarefas'), 
    
    path('adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
    
    path('concluir/<int:tarefa_id>/', views.marcar_concluida, name='marcar_concluida'),
    
    path('remover/<int:tarefa_id>/', views.remover_tarefa, name='remover_tarefa'),
]