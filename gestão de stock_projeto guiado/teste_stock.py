import os

import bd
import stock

bd.FICHEIRO = "teste.db"        # não mexe na loja a sério
if os.path.exists(bd.FICHEIRO):
    os.remove(bd.FICHEIRO)      # cada teste começa do zero
bd.criar_tabelas()
stock.carregar_exemplo()

print("Produtos:", len(stock.listar_produtos()))
print("Stock TECL-02:", stock.procurar("tecl-02")["stock"])

novo = stock.registar_movimento("tecl-02", "saida", 2, "venda")
print("Depois da venda:", novo)

pedidos = [
    ("TECL-02", "saida", 5),    # mais do que há
    ("XPTO", "entrada", 1),     # código que não existe
    ("RATO-01", "saida", 0),    # quantidade inválida
]
for codigo, tipo, quantidade in pedidos:
    try:
        stock.registar_movimento(codigo, tipo, quantidade)
        print("Aceite:", codigo)
    except ValueError as erro:
        print("Recusado:", erro)

try:
    stock.adicionar_produto("rato-01", "Outro rato", 9.9)
except ValueError as erro:
    print("Recusado:", erro)

print("Em falta:", [p["codigo"] for p in stock.em_falta()])
print("Movimentos:", len(stock.movimentos("TECL-02")))
