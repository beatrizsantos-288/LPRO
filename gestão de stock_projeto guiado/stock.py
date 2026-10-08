"""Regras da loja: produtos, movimentos de stock e alertas.

Não tem input() nem print(): só recebe valores e devolve
resultados. Quando uma regra falha, lança ValueError.
"""
import sqlite3
from datetime import date

from bd import ligacao


def adicionar_produto(codigo, nome, preco, minimo=0):
    """Cria um produto com stock 0 e devolve o id."""
    codigo = codigo.strip().upper()
    nome = nome.strip()
    if not codigo or not nome:
        raise ValueError("o código e o nome são obrigatórios")
    if preco < 0 or minimo < 0:
        raise ValueError("o preço e o mínimo não podem ser negativos")
    try:
        with ligacao() as con:
            cur = con.execute(
                "INSERT INTO produtos (codigo, nome, preco, minimo) "
                "VALUES (?, ?, ?, ?)",
                (codigo, nome, preco, minimo),
            )
    except sqlite3.IntegrityError:
        raise ValueError(f"já existe um produto {codigo}") from None
    return cur.lastrowid


def procurar(codigo):
    """Devolve o produto com esse código, ou None."""
    with ligacao() as con:
        return con.execute(
            "SELECT * FROM produtos WHERE codigo = ?",
            (codigo.strip().upper(),),
        ).fetchone()


def listar_produtos():
    with ligacao() as con:
        return con.execute(
            "SELECT * FROM produtos ORDER BY codigo"
        ).fetchall()


def registar_movimento(codigo, tipo, quantidade, nota=""):
    """Regista uma entrada ou saída e devolve o stock novo."""
    if tipo not in ("entrada", "saida"):
        raise ValueError("o tipo tem de ser entrada ou saida")
    if quantidade <= 0:
        raise ValueError("a quantidade tem de ser maior que zero")
    produto = procurar(codigo)
    if produto is None:
        raise ValueError(f"não existe o produto {codigo}")
    variacao = quantidade if tipo == "entrada" else -quantidade
    try:
        with ligacao() as con:   # os dois passos: ambos ou nenhum
            con.execute(
                "INSERT INTO movimentos "
                "(produto_id, tipo, quantidade, data, nota) "
                "VALUES (?, ?, ?, ?, ?)",
                (produto["id"], tipo, quantidade,
                 date.today().isoformat(), nota),
            )
            con.execute(
                "UPDATE produtos SET stock = stock + ? WHERE id = ?",
                (variacao, produto["id"]),
            )
    except sqlite3.IntegrityError:
        # o CHECK (stock >= 0) falhou: o INSERT também foi desfeito
        raise ValueError(
            f"stock insuficiente, {produto['nome']} tem {produto['stock']}"
        ) from None
    return produto["stock"] + variacao


def em_falta():
    """Produtos com stock igual ou abaixo do mínimo."""
    with ligacao() as con:
        return con.execute(
            "SELECT codigo, nome, stock, minimo FROM produtos "
            "WHERE stock <= minimo ORDER BY stock - minimo, codigo"
        ).fetchall()


def movimentos(codigo, limite=5):
    """Últimos movimentos de um produto, do mais recente para trás."""
    with ligacao() as con:
        return con.execute(
            "SELECT m.data, m.tipo, m.quantidade, m.nota "
            "FROM movimentos AS m "
            "JOIN produtos AS p ON p.id = m.produto_id "
            "WHERE p.codigo = ? ORDER BY m.id DESC LIMIT ?",
            (codigo.strip().upper(), limite),
        ).fetchall()


def relatorio():
    """Devolve (linhas, valor total) para o relatório de stock."""
    with ligacao() as con:
        linhas = con.execute(
            "SELECT codigo, nome, stock, minimo, "
            "stock * preco AS valor FROM produtos ORDER BY nome"
        ).fetchall()
    total = sum(p["valor"] for p in linhas)
    return linhas, total


EXEMPLO = [
    # código, nome, preço, mínimo, stock inicial
    ("RATO-01", "Rato sem fios", 14.90, 5, 12),
    ("TECL-02", "Teclado USB", 20.00, 5, 3),
    ("PEN-64", "Pen USB 64 GB", 9.50, 8, 0),
    ("HDMI-2M", "Cabo HDMI 2 m", 6.90, 10, 25),
    ("MON-24", 'Monitor 24"', 129.00, 2, 4),
]


def carregar_exemplo():
    """Cria os produtos de exemplo, se a loja estiver vazia."""
    if listar_produtos():
        return False
    for codigo, nome, preco, minimo, inicial in EXEMPLO:
        adicionar_produto(codigo, nome, preco, minimo)
        if inicial > 0:
            registar_movimento(codigo, "entrada", inicial, "stock inicial")
    return True


if __name__ == "__main__":
    print("stock.py é um módulo: só define funções.")
    print("Executa o teste_stock.py ou o app.py.")
