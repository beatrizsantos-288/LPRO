import sqlite3

# 1. Ligar: abre o ficheiro (cria-o se não existir)
con = sqlite3.connect("escola.db")

# 2. Executar: várias instruções de uma vez
con.executescript("""
CREATE TABLE IF NOT EXISTS turmas (
    id   INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE,
    ano  INTEGER NOT NULL CHECK (ano BETWEEN 10 AND 12)
);
CREATE TABLE IF NOT EXISTS alunos (
    id       INTEGER PRIMARY KEY,
    numero   INTEGER NOT NULL,
    nome     TEXT NOT NULL,
    email    TEXT UNIQUE,
    turma_id INTEGER REFERENCES turmas(id),
    media    REAL
);
""")

# 4. Confirmar e 5. fechar
con.commit()
con.close()
print("Base de dados escola.db pronta.")
