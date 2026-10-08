# Variáveis: um nome que guarda um valor
#Exemplo 1 explicando os tipoos  de dados
produto = "Rato sem fios"  
quantidade = 12             # int: número inteiro
preco = 14.9                # float: número decimal (usa ponto)
disponivel = True           # bool: verdadeiro ou falso
fornecedor = None           # None: ainda sem valor

print(produto, quantidade, preco, disponivel, fornecedor)
print(type(produto), type(quantidade), type(preco))
print(type(disponivel), type(fornecedor))


#Exemplo 2 explicando a função input faznedo junção
"""Aqui esta a pedir ao utilizador para inserir dois numero e o a + b
serve para juntar os dois valores e somar os dois valores"""

a = input("Primeiro número: ")
b = input("Segundo número: ")
print("Sem converter:", a + b)
print("Convertido:", int(a) + int(b))



#Exemplo 3 explicando as operações matemáticas divisao...
"""Aqui vamosn utilizar operações matemáticas para compreender melhor
"""
minutos = 135
print(minutos / 60)     # divisão normal
print(minutos // 60)    # divisão inteira
print(minutos % 60)     # resto
print(2 ** 10)          # potência
print(round(7 / 3, 2))  # arredondar a 2 casas

horas = minutos // 60
resto = minutos % 60
print(f"{minutos} minutos são {horas} h e {resto} min")



#Exemplo 4 explicando a formatação de f-strings
nome = "Teclado USB"
preco = 20

print(f"{nome} custa {preco:.2f} €, com IVA {preco * 1.23:.2f} €")
print(f"[{nome:<15}]")      # alinhado à esquerda em 15 posições
print(f"[{nome:>15}]")      # alinhado à direita
print(f"[{preco:>8.2f}]")   # 8 posições e 2 casas decimais
print(f"{preco:.2f} €".replace(".", ","))  # vírgula decimal



#Exemplo 5 - Decisão usando if elif else
nota = float(input("Nota (0 a 20): "))

if nota < 0 or nota > 20:
    print("Nota inválida.")
elif nota >= 17.5:
    print("Muito bom")
elif nota >= 14:
    print("Bom")
elif nota >= 9.5:
    print("Suficiente")
else:
    print("Insuficiente")



#Exemplo 6 - Ciclos usando for
""" Tabela de preços com IVA de 1 a 5 unidades
"""
preco = 8.25
for unidades in range(1, 6):
    total = unidades * preco * 1.23
    print(f"{unidades} un. = {total:6.2f} €")



#Exemplo 7 - Ciclos usando while enquanto for verdadeira 
stock = 6
dias = 0
while stock > 0:
    dias += 1
    stock -= 4
    print(f"Dia {dias}: restam {max(stock, 0)} unidades")
print("Esgotado ao fim de", dias, "dias")

