"""Exeemplo de try/execept, que permite tratar erros e continuar a execução do programa"""

def ler_inteiro(pergunta, minimo=None, maximo=None):
    """Pede um inteiro até o utilizador escrever um valor válido."""
    while True:
        texto = input(pergunta)
        try:
            valor = int(texto)
        except ValueError:
            print(f"  '{texto}' não é um número inteiro.")
            continue
        if minimo is not None and valor < minimo:
            print(f"  Tem de ser pelo menos {minimo}.")
        elif maximo is not None and valor > maximo:
            print(f"  Não pode passar de {maximo}.")
        else:
            return valor


idade = ler_inteiro("Idade: ", minimo=15, maximo=99)
print("Idade registada:", idade)
