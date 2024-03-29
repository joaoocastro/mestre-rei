# mestre-rei
entre na pasta mestre-rei usando terminal

cd \Users\joaoc\Documents\workspace\mestre-rei

# execute o comando no terminal para liberar acessos
powershell -executionpolicy Unrestricted


# comando para iniciar o servidor backend do django, sempre dentro da pasta mestre-rei
python manage.py runserver

# com o servidor iniciado vá aos endereços
http://localhost:8000/
http://localhost:8000/admin
http://localhost:8000/login
http://localhost:8000/signup
http://localhost:8000/barbeiros
http://localhost:8000/barbeiros/add
etc ...

# comando para gerar as tabelas apos fazer alguma alteraçao no arquivo app/models.py
python manage.py makemigrations app
python manage.py migrate app