import sqlite3

con = sqlite3.connect("escola.db")
aluno_id = int(input("Id do aluno: "))
nova = float(input("Nova média: "))

cur = con.execute(
    "UPDATE alunos SET media = ? WHERE id = ?",
    (nova, aluno_id),
)
con.commit()
if cur.rowcount == 0:
    print("Não existe nenhum aluno com esse id.")
else:
    print(f"Média atualizada ({cur.rowcount} linha).")
con.close()
