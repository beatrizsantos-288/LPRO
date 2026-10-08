import sqlite3

con = sqlite3.connect("escola.db")
con.execute("PRAGMA foreign_keys = ON")   # em cada ligação

novos = [
    (5, "Inês Rocha", "ana@escola.pt", 3),   # email repetido
    (6, "João Vaz", "joao@escola.pt", 99),   # turma não existe
    (7, "Lara Reis", "lara@escola.pt", 3),   # tudo certo
]
for numero, nome, email, turma in novos:
    try:
        con.execute(
            "INSERT INTO alunos (numero, nome, email, turma_id) "
            "VALUES (?, ?, ?, ?)",
            (numero, nome, email, turma),
        )
        con.commit()
        print(f"{nome}: gravado")
    except sqlite3.IntegrityError as erro:
        print(f"{nome}: recusado ({erro})")
con.close()
