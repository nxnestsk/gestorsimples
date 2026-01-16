from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Tarefa, Categoria
from datetime import datetime


def lista_tarefas(request):
    """Exibe a lista de tarefas com filtros e pesquisa."""
    tarefas = Tarefa.objects.all()
    categorias = Categoria.objects.all()

    # Pesquisa
    pesquisa = request.GET.get('pesquisa', '')
    if pesquisa:
        tarefas = tarefas.filter(
            Q(titulo__icontains=pesquisa) | Q(descricao__icontains=pesquisa)
        )

    # Filtro por status
    filtro_status = request.GET.get('status', '')
    if filtro_status:
        tarefas = tarefas.filter(status=filtro_status)

    # Filtro por prioridade
    filtro_prioridade = request.GET.get('prioridade', '')
    if filtro_prioridade:
        tarefas = tarefas.filter(prioridade=filtro_prioridade)

    # Filtro por categoria
    filtro_categoria = request.GET.get('categoria', '')
    if filtro_categoria:
        tarefas = tarefas.filter(categoria_id=filtro_categoria)

    context = {
        'tarefas': tarefas,
        'categorias': categorias,
        'pesquisa': pesquisa,
        'filtro_status': filtro_status,
        'filtro_prioridade': filtro_prioridade,
        'filtro_categoria': filtro_categoria,
    }
    return render(request, 'todo/lista_tarefas.html', context)


def adicionar_tarefa(request):
    """Adiciona uma nova tarefa com todos os campos do formulário."""
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_limite_str = request.POST.get('data_limite')
        prioridade = request.POST.get('prioridade', 'Media')
        categoria_id = request.POST.get('categoria')

        data_limite = None
        if data_limite_str:
            try:
                data_limite = datetime.strptime(data_limite_str, '%Y-%m-%d').date()
            except ValueError:
                pass

        categoria = None
        if categoria_id:
            categoria = Categoria.objects.filter(id=categoria_id).first()

        Tarefa.objects.create(
            titulo=titulo,
            descricao=descricao,
            data_limite=data_limite,
            prioridade=prioridade,
            categoria=categoria
        )
        return redirect('lista_tarefas')

    return redirect('lista_tarefas')


def editar_tarefa(request, tarefa_id):
    """Edita uma tarefa existente."""
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.prioridade = request.POST.get('prioridade', 'Media')

        data_limite_str = request.POST.get('data_limite')
        if data_limite_str:
            try:
                tarefa.data_limite = datetime.strptime(data_limite_str, '%Y-%m-%d').date()
            except ValueError:
                pass
        else:
            tarefa.data_limite = None

        categoria_id = request.POST.get('categoria')
        if categoria_id:
            tarefa.categoria = Categoria.objects.filter(id=categoria_id).first()
        else:
            tarefa.categoria = None

        tarefa.save()
        return redirect('lista_tarefas')

    return render(request, 'todo/editar_tarefa.html', {
        'tarefa': tarefa,
        'categorias': categorias
    })


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


def adicionar_categoria(request):
    """Adiciona uma nova categoria."""
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cor = request.POST.get('cor', '#6c757d')
        if nome:
            Categoria.objects.get_or_create(nome=nome, defaults={'cor': cor})
    return redirect('lista_tarefas')


def remover_categoria(request, categoria_id):
    """Remove uma categoria."""
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    return redirect('lista_tarefas')