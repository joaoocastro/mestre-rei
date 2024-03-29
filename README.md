# mestre-rei
entre na pasta mestre-rei usando terminal

cd \Users\joaoc\Documents\workspace\mestre-rei

# execute o comando no terminal para liberar acessos
powershell -executionpolicy Unrestricted


# comando para iniciar o servidor backend do django
python manage.py runserver

# com o servidor iniciado vá ao endereço
http://localhost:8000/
http://localhost:8000/admin
http://localhost:8000/login
http://localhost:8000/home
http://localhost:8000/barbeiros
etc ...

# comando para gerar as tabelas
python manage.py makemigrations app
python manage.py migrate app