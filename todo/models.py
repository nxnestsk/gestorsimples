from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    cor = models.CharField(max_length=7, default='#6c757d')  # Cor hex

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Categorias"


class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    data_limite = models.DateField(blank=True, null=True)

    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Concluida', 'Concluída'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pendente',
    )

    PRIORIDADE_CHOICES = [
        ('Alta', 'Alta'),
        ('Media', 'Média'),
        ('Baixa', 'Baixa'),
    ]
    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES,
        default='Media',
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='tarefas'
    )

    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['status', '-prioridade', 'data_limite', '-data_criacao']