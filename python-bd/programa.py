import sqlite3

con = sqlite3.connect("escola.db")

cursor = con.execute("SELECT * FROM alunos")

for aluno in cursor:
    print(aluno)

con.close()