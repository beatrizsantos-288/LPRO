import sqlite3

con = sqlite3.connect(":memory:")   # base de dados só em memória
con.executescript("""
CREATE TABLE utilizadores (nome TEXT, senha TEXT);
INSERT INTO utilizadores VALUES ('ana', 'segredo1');
INSERT INTO utilizadores VALUES ('rui', 'segredo2');
""")
senha = input("Senha: ")

# Errado: o texto do utilizador entra no SQL
sql = f"SELECT nome FROM utilizadores WHERE senha = '{senha}'"
print("SQL enviado:", sql)
print("Entrou como:", con.execute(sql).fetchall())

# Certo: o valor segue à parte, num parâmetro
cur = con.execute(
    "SELECT nome FROM utilizadores WHERE senha = ?", (senha,)
)
print("Com parâmetro:", cur.fetchall())
