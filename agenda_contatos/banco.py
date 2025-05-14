import sqlite3

def conectar():
    return sqlite3.connect("contatos.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT,
            telefone TEXT
        )
    """)
    conn.commit()
    conn.close()

def inserir(nome, email, telefone):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contatos (nome, email, telefone) VALUES (?, ?, ?)", (nome, email, telefone))
    conn.commit()
    conn.close()

def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatos")
    dados = cursor.fetchall()
    conn.close()
    return dados

def deletar(id_contato):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contatos WHERE id = ?", (id_contato,))
    conn.commit()
    conn.close()

def atualizar(id_contato, nome, email, telefone):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE contatos SET nome=?, email=?, telefone=? WHERE id=?", (nome, email, telefone, id_contato))
    conn.commit()
    conn.close()

def buscar_por_nome(nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatos WHERE nome LIKE ?", (f"%{nome}%",))
    resultado = cursor.fetchall()
    conn.close()
    return resultado
