import _sqlite3

# CONECTA COM O ARQUIVO DE DADOS
banco = _sqlite3.connect('banco.db')

# CURSOS PARA EXECUTAR COMANDOS
sql = banco.cursor()

# RECUPERANDO TODOS AS COLUNAS DA TABELA
sql.execute('SELECT * FROM alunos')

# RECUPERANDO ALGUMAS COLUNAS DA TABELA
sql.execute('SELECT nome, curso FROM alunos')

# FILTRANDO INFORMAÇÕES
sql.execute('SELECT curso, nome, cidade FROM alunos where cidade="Olímpia"')

# FILTRANDO PELA IDADE
sql.execute('SELECT * FROM alunos where idade <= 19')

# EXCLUINDO VALORES DA CONSULTA
sql.execute('SELECT * FROM alunos where cidade <> "Olímpia"')

# ORDENANDO VALORES ASC E DESC
sql.execute('SELECT * FROM alunos ORDER BY nome')

# RANKING NA CONSULTA
sql.execute('SELECT * FROM alunos ORDER BY nota ASC LIMIT 3')

for row in sql.fetchall():
    #print(f'NOME: {row[0]}, IDADE: {row[1]}, CIDADE: {row[2]}, CURSO: {row[3]}')
    print(f'NOME: {row[0]}')
    print(f'IDADE: {row[1]}')
    print(f'CURSO: {row[2]}')
    print(f'CIDADE: {row[3]}')
    print(f'NOTA: {row[4]}')
    print('----------------------------------')