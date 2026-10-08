def retirar(stock, quantidade):
    if quantidade <= 0:
        raise ValueError("a quantidade tem de ser positiva")
    if quantidade > stock:
        raise ValueError(f"só há {stock} unidades")
    return stock - quantidade


for pedido in (2, 9, -1):
    try:
        print("Ficam", retirar(5, pedido))
    except ValueError as erro:
        print("Recusado:", erro)
