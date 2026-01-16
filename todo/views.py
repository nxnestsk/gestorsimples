from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from datetime import datetime

def lista_tarefas(request):
    """Exibe a lista de tarefas, ordenada por status e prazo."""
   
    tarefas = Tarefa.objects.all() 
    return render(request, 'todo/lista_tarefas.html', {'tarefas': tarefas})

def adicionar_tarefa(request):
    """Adiciona uma nova tarefa com todos os campos do formulário."""
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_limite_str = request.POST.get('data_limite')
        
        data_limite = None
        if data_limite_str:
            try:
               
                data_limite = datetime.strptime(data_limite_str, '%Y-%m-%d').date()
            except ValueError:
                pass

        Tarefa.objects.create(
            titulo=titulo,
            descricao=descricao,
            data_limite=data_limite
        )
 
        return redirect('lista_tarefas')

    return redirect('lista_tarefas') 

def marcar_concluida(request, tarefa_id):
    """Marca uma tarefa como concluída."""
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'Concluida'
    tarefa.save()
    return redirect('lista_tarefas')

def remover_tarefa(request, tarefa_id):
    """Remove uma tarefa do banco de dados."""
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('lista_tarefas')