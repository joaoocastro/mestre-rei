Set-ExecutionPolicy RemoteSigned

# dentro da pasta mestre-rei inicie o ambiente virtual do python
.\venv\Scripts\activate

## vai aparecer assim - > (venv) PS C:\Users\joaoc\Documents\workspace\mestre-rei>


## GIT
git status (ver arquivos alterados)
git add .
git commit -m 'mensagem'
git push (empurrar, enviar)

# GIT PEGAR DA NUVEM
git pull (pegar, puxar)

# mestre-rei
entre na pasta mestre-rei usando terminal

cd \Users\joaoc\Documents\workspace\mestre-rei

# execute o comando no terminal para liberar acessos
powershell -executionpolicy Unrestricted


# comando para iniciar o servidor backend do django, sempre dentro da pasta mestre-rei
python manage.py runserver

# com o servidor iniciado vá aos endereços
http://localhost:8000/
http://localhost:8000/login
http://localhost:8000/signup
http://localhost:8000/barbeiros
http://localhost:8000/barbeiros/add
http://localhost:8000/clientes/add/
etc ...

