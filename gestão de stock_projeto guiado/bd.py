"""Ligação à base de dados e criação das tabelas."""
import sqlite3
from contextlib import contextmanager

FICHEIRO = "loja.db"

ESQUEMA = """
CREATE TABLE IF NOT EXISTS produtos (
    id      INTEGER PRIMARY KEY,
    codigo  TEXT NOT NULL UNIQUE,
    nome    TEXT NOT NULL,
    preco   REAL NOT NULL CHECK (preco >= 0),
    stock   INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
    minimo  INTEGER NOT NULL DEFAULT 0 CHECK (minimo >= 0)
);
CREATE TABLE IF NOT EXISTS movimentos (
    id         INTEGER PRIMARY KEY,
    produto_id INTEGER NOT NULL REFERENCES produtos(id),
    tipo       TEXT NOT NULL CHECK (tipo IN ('entrada', 'saida')),
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    data       TEXT NOT NULL,
    nota       TEXT NOT NULL DEFAULT ''
);
"""


@contextmanager
def ligacao():
    """Abre a base de dados e, no fim do bloco with:
    grava tudo se correu bem, desfaz tudo se houve erro
    e fecha sempre a ligação."""
    con = sqlite3.connect(FICHEIRO)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    try:
        with con:        # commit ou rollback
            yield con    # aqui corre o bloco de quem chamou
    finally:
        con.close()      # fecha sempre


def criar_tabelas():
    with ligacao() as con:
        con.executescript(ESQUEMA)


if __name__ == "__main__":
    criar_tabelas()
    with ligacao() as con:
        tabelas = con.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'"
        ).fetchall()
    print("Base de dados:", FICHEIRO)
    print("Tabelas:", ", ".join(t["name"] for t in tabelas))
