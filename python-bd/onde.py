import sqlite3
from pathlib import Path

PASTA = Path(__file__).parent      # a pasta onde está este ficheiro .py
FICHEIRO = PASTA / "escola.db"     # o .db ao lado dele

print("Pasta do programa:", PASTA.name)
print("Ficheiro:", FICHEIRO.name, "| já existe?", FICHEIRO.exists())
print("Terminal aberto em:", Path.cwd().name)

con = sqlite3.connect(FICHEIRO)    # abre sempre o mesmo ficheiro
n = con.execute("SELECT COUNT(*) FROM alunos").fetchone()[0]
print("Alunos gravados:", n)
con.close()
