import sqlite3

con = sqlite3.connect("escola.db")

# Os mesmos dados do capítulo 7, agora carregados pelo Python.
turmas = [
    (1, "10A", 10),
    (2, "11A", 11),
    (3, "12A", 12),
]
alunos = [
    # id, número, nome, email, turma, média
    (1, 1, "Ana Costa",    "ana@escola.pt",    3, 16.4),
    (2, 2, "Bruno Dias",   "bruno@escola.pt",  3, 12.8),
    (3, 3, "Carla Mendes", None,               3, 17.9),
    (4, 1, "Diogo Faria",  "diogo@escola.pt",  2, 9.6),
    (5, 2, "Eva Lopes",    "eva@escola.pt",    2, 14.1),
    (6, 1, "Filipe Rocha", "filipe@escola.pt", 1, None),
    (7, 3, "Gabriela Sá",  "gabi@escola.pt",   None, 11.5),
]

con.executemany(
    "INSERT OR IGNORE INTO turmas (id, nome, ano) VALUES (?, ?, ?)",
    turmas,
)
con.executemany(
    "INSERT OR IGNORE INTO alunos "
    "(id, numero, nome, email, turma_id, media) "
    "VALUES (?, ?, ?, ?, ?, ?)",
    alunos,
)
con.commit()

total = con.execute("SELECT COUNT(*) FROM alunos").fetchone()[0]
print(f"{len(turmas)} turmas e {total} alunos na base de dados.")
con.close()
