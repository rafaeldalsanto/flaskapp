# Executar a aplicação
Para executar a aplicação execute:
```
python run.py
```

ou se preferir usar o Flask CLI:
```
export FLASK_APP=flaskapp
flask run
```


# Migrations
As migrações são gerenciadas pela lib `Flask-Migrate`.


1. Criar a pasta migrations (executado apenas uma vez):
    ```
    flask db init
    ```

2. Gerar uma migração:
    ```
    flask db migrate
    ```

3. Aplicar as migrações pendentes no BD:
    ```
    flask db upgrade
    ```
