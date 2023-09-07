# importando SQLite3
import sqlite3

# criando conexao com o banco de dados
try:
    conexao = sqlite3.connect('cadastro_fabrilan.db')
    print("Conexao com o banco de dados realizada com sucesso!")
except sqlite3.Error:
    print("Erro ao conectar ao banco de dados!", e)

# criando tabela de cursos
try:
    with conexao:
        cur = conexao.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            duracao TEXT,
            preco REAL
        )""")

        print("Tabela de cursos criada com sucesso!")

except sqlite3.Error:
    print("Erro ao criar tabela de cursos!", e)

# criando tabela de turmas
try:
    with conexao:
        cur = conexao.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS turmas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            curso_nome TEXT,
            data_inicio DATE,
            FOREIGN KEY (curso_nome) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE
        )""")

        print("Tabela de turmas criada com sucesso!")

except sqlite3.Error:
    print("Erro ao criar tabela de cursos!", e)

# criando tabela de alunos
try:
    with conexao:
        cur = conexao.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            sexo TEXT,
            imagem TEXT,
            data_nascimento DATE,
            cpf TEXT,
            turma_nome TEXT,
            FOREIGN KEY (turma_nome) REFERENCES turmas (nome) ON DELETE CASCADE
        )""")

        print("Tabela de alunos criada com sucesso!")

except sqlite3.Error:
    print("Erro ao criar tabela de Alunos!", e)
