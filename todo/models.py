from django.db import models

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
    data_criacao = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.titulo

    class Meta:
        
        ordering = ['status', 'data_limite', '-data_criacao']