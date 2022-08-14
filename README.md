# Projeto-Curso-de-Django
## Projeto do curso de Django pelo YouTube

### Aula 17:
ForeignKey entre User e Task

Delimitar as tarefas para cada usuário.
- Criar o botão para registrar:
nos arquivos de autenticação(login.html e register.html)
Models – foreignkey() 

Comando para o prompt:
 - Python .\manage.py makemigrations
 - Python .\manage.py migrate

Duas modificações nas views:
-	Filtrar as tarefas pelo id do usuário.(Search, if e else)

Criar a função do id para as adições de tarefa do usuário.(views)

