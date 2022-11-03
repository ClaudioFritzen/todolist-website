Projeto de lista de tarefas
Projeto FullStack utilizando as tecnologias HTML, Python e Django

--- Como rodar esse projeto na sua máquina ----
1° Baixe o projeto ou faça um clone
2° Crie seu ambiente virtual para evitar conflitos externos
3° Rode o comando no terninal da sua IDE






---- Fazendo deploy no heroku

1. Construa o seu projeto Django
2. Instalar a lib gunicorn e django_heroku

3. Na Raiz do projeto
    --> Crie na base do projeto um arquivo chamado runtime.txt
        --> Rode no terminal o comando python --version para saber a versao do python que esta utilizando 
            --> Pegue a versão e coloca no arquivo runtime.txt
                    python-3.10.5

4. Crie o arquivo Procfile
    No arquivo Procfile escreva o seguinte comando
        ---> Escreva: web gunicorn projectname.wsgi:application --log-file -   
        Como saber o nome do meu projeto... 
        Provavelmente será o que tem o arquivo settings.py

5. Rode o seguinte comando para gerar o requirements
    pip freeze > requirements.txt

6. No arquivo settings.py
    No inicio:
        import os
        import django_heroku
        import dj_database_url
    
    Configure os arquivos staticos
        --> STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
        --> STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
    OBS: não esqueca da virgula entre os parenteses ela é muito importante

    ABAIXO ESCREVA
        django_heroku.settings(locals())

7. Baixar o git
8. Criar uma conta no Heroku
9. Criar um app no Heroku
10. Criar uma conta no github
11. Criar um repostitório no github
12. Voltar no heroku e fazer deploy via github
