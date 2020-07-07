import sqlite3

# CRIANDO O BANCO DE DADOS
banco = sqlite3.connect('banco.db')

# O cursor() EXECUTA COMANDOS NO SQLite
cursor = banco.cursor()

# CRIANDO UMA TABELA
cursor.execute("CREATE TABLE pessoas (nome TEXT, idade INTEGER, cidade TEXT)")

# EXECUTA OS COMANDOS DA FILA
banco.commit()

# INSERINDO DADOS NA TABELA
cursor.execute("INSERT INTO pessoas VALUES ('Steffany', 19, 'Olímpia')")

cursor.execute("SELECT * FROM pessoas")
print('TABELA PESSOAS:')
print(cursor.fetchall())