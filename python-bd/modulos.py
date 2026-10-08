"""Funções de cálculo usadas em vários programas."""
IVA = 23


def preco_com_iva(preco, taxa=IVA):
    return round(preco * (1 + taxa / 100), 2)


def euros(valor):
    return f"{valor:.2f} €".replace(".", ",")
