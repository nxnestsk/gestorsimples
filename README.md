# Gestor Simples

Um gestor de tarefas minimalista construído com Django.

## Funcionalidades

- Criar tarefas com título, descrição e data limite
- Editar tarefas existentes
- Marcar tarefas como concluídas
- Remover tarefas
- Definir prioridades (Alta, Média, Baixa)
- Criar categorias com cores personalizadas
- Pesquisar tarefas por texto
- Filtrar por status, prioridade e categoria
- Ordenação automática por status, prioridade e prazo

## Requisitos

- Python 3.x
- Django 5.2+

## Instalação

```bash
# Clonar o repositório
git clone https://github.com/nxnestsk/gestorsimples.git
cd gestorsimples

# Instalar dependências
pip install django

# Aplicar migrações
python manage.py migrate

# Iniciar o servidor
python manage.py runserver
```

## Uso

Acesse `http://127.0.0.1:8000/` no navegador.

## Tecnologias

- Python
- Django
- HTML/CSS

## Autor

**nxnestsk**

## Licença

MIT
