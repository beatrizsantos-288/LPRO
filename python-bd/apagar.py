import sqlite3

con = sqlite3.connect("escola.db")

aluno_id = int(input("Id do aluno a apagar: "))

aluno = con.execute(
    "SELECT nome FROM alunos WHERE id = ?", (aluno_id,)
).fetchone()

if aluno is None:
    print("Esse aluno não existe.")
else:
    print("Aluno encontrado:", aluno[0])

    resposta = input("Quer apagar este aluno? (s/n): ")

    if resposta.lower() == "s":
        con.execute(
            "DELETE FROM alunos WHERE id = ?", (aluno_id,)
        )

        con.commit()

        print("Aluno apagado com sucesso!")
    else:
        print("Cancelado.")

con.close()