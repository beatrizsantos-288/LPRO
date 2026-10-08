import sqlite3

con = sqlite3.connect("escola.db")
cur = con.execute(
    "SELECT numero, nome, media FROM alunos "
    "WHERE turma_id = ? ORDER BY numero",
    (3,),
)
linhas = cur.fetchall()          # lista de tuplos
print(f"{len(linhas)} alunos na turma 3")
print(f"{'Nº':>3}  {'Nome':<14} {'Média':>6}")
for numero, nome, media in linhas:
    texto = f"{media:.1f}" if media is not None else "-"
    print(f"{numero:>3}  {nome:<14} {texto:>6}")

um = con.execute(
    "SELECT nome, email FROM alunos WHERE id = ?", (1,)
).fetchone()                     # um tuplo, ou None
print("\nAluno 1:", um)
con.close()
