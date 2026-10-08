"""Exemplo de funções que calculamos o preço do IVA, utilizamos a função def"""

def preco_com_iva(preco, taxa=23):
    """Devolve o preço com IVA, arredondado ao cêntimo."""
    return round(preco * (1 + taxa / 100), 2)


def euros(valor):
    """Formata 1234.5 como '1234,50 €'."""
    return f"{valor:.2f} €".replace(".", ",")


print(euros(preco_com_iva(10)))
print(euros(preco_com_iva(10, taxa=6)))
print(euros(preco_com_iva(7.25)))
