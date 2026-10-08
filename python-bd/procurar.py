import sqlite3

con = sqlite3.connect("escola.db")
con.row_factory = sqlite3.Row        # linhas com nomes

email = input("Email a procurar: ").strip().lower()
aluno = con.execute(
    "SELECT * FROM alunos WHERE email = ?", (email,)
).fetchone()

if aluno is None:
    print("Não encontrado.")
else:
    print(aluno["nome"], "tem média", aluno["media"])
    print("Colunas:", aluno.keys())
    print(dict(aluno))
con.close()
