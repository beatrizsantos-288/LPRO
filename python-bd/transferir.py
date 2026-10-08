import sqlite3

con = sqlite3.connect(":memory:")
con.execute("""CREATE TABLE contas (
    nome  TEXT PRIMARY KEY,
    saldo REAL NOT NULL CHECK (saldo >= 0))""")
con.executemany("INSERT INTO contas VALUES (?, ?)",
                [("Ana", 100), ("Rui", 20)])
con.commit()


def transferir(origem, destino, valor):
    try:
        with con:  # commit se correr bem, rollback se falhar
            con.execute("UPDATE contas SET saldo = saldo + ? "
                        "WHERE nome = ?", (valor, destino))
            con.execute("UPDATE contas SET saldo = saldo - ? "
                        "WHERE nome = ?", (valor, origem))
        print(f"Transferidos {valor} € de {origem} para {destino}.")
    except sqlite3.IntegrityError:
        print(f"Recusado: {origem} não tem saldo para {valor} €.")


transferir("Ana", "Rui", 30)
transferir("Rui", "Ana", 500)
print(con.execute("SELECT * FROM contas").fetchall())
