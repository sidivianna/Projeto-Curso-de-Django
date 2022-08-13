# Projeto-Curso-de-Django
## Projeto do curso de Django pelo YouTube

### Aula 8:
Aplicação e funcionamento das migrations e dos models, além das ligações entre eles ni projeto.

Models e Migrations
- Model: é um arquivo que vai conter informações de alguma coisa (post de um blog), ou uma tarefa  (uma task). (título, data de criação, atualização, processo terminado ou não.
Arquivo depois de escrito vira uma migration no banco de dados.(não precisando trabalhar com sql)

Migrations: 
- após criados os comandos para banco de dados, se trensfere o código em python para uma instrução em sql.(em um arquivo migrations) Após isso é possível migrar esses arquivos para as tabelas do banco de dados.
Cria um arquivo sql com as instruções criadas no arquivo de models.

Comando: (para o terminal)
- python .\manage.py makemigrations
- python .\manage.py migrate
para criar um usuário admin
- username: admin
- email: admin@admin.com
- senha:01234

python .\manage.py createsuperuser	


