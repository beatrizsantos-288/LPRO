import sqlite3

con = sqlite3.connect("escola.db")
con.row_factory = sqlite3.Row

procura = input("Parte do nome: ").strip()

# O % faz parte do VALOR, nunca do texto do SQL
linhas = con.execute(
    "SELECT nome, email FROM alunos "
    "WHERE nome LIKE ? ORDER BY nome",
    (f"%{procura}%",),
).fetchall()

print(f"{len(linhas)} resultado(s):")
for a in linhas:
    print(" -", a["nome"], "|", a["email"] or "sem email")

# Parâmetros com nome: :minimo e :turma, com um dicionário
melhores = con.execute(
    "SELECT nome, media FROM alunos "
    "WHERE media >= :minimo AND turma_id = :turma "
    "ORDER BY media DESC",
    {"minimo": 13, "turma": 3},
).fetchall()

print("\nNa turma 3 com média igual ou acima de 13:")
for a in melhores:
    print(f" - {a['nome']:<14} {a['media']:>5.1f}")
con.close()
