# Sistema de Registo de Miniaturas
Este projeto é um sistema de resgistro de miniaturas com Python utilizando MySQL.

# Tecnologias utilizadas
- Python
- MySQL

# Bibliotecas utilizdas
- Tkinter
- MySQL Connector

# Como executar este projeto
- Clone o repositório
```
git clone git@github.com:mathslima/registro-minis.git
```
  
- Crie uma base de dados no MySQL chamada miniaturas com uma tabela chamada minis, conforme arquivo 
```
miniaturas.mini.sql
```

- Altere os dados de usuário e senha na conexão do banco de dados na main.py
```
user = 'seu_usuario'
password = 'sua_senha'
```

#### -Extra
- Para carregar uma lista com diversos dados no banco, utilize o arquivo
```
load_database.py
```