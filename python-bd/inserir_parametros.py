import sqlite3

con = sqlite3.connect("escola.db")

turmas = [(1, "10A", 10), (2, "11A", 11), (3, "12A", 12)]
con.executemany(
    "INSERT OR IGNORE INTO turmas (id, nome, ano) VALUES (?, ?, ?)",
    turmas,
)

nome = input("Nome do aluno: ")
numero = int(input("Número: "))
turma = int(input("Turma (1, 2 ou 3): "))

cur = con.execute(
    "INSERT INTO alunos (numero, nome, turma_id) VALUES (?, ?, ?)",
    (numero, nome, turma),
)
con.commit()
print(f"Aluno {nome} gravado com o id {cur.lastrowid}.")
con.close()
