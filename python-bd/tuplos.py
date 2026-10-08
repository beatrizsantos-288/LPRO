"""  Exemplo de tuplos, que permite guardar dados do aluno e o desempacotar 
que pegar nos valores que estão dentro de uma estrutura(tuplo) e colocar em variáveis separadas"""

# Uma linha de uma tabela, tal como o sqlite3 a devolve
linha = (7, "Gabriela Sá", 11.5)
numero, nome, media = linha        # desempacotar
print(f"{numero}: {nome} tem média {media}")

# Uma tabela inteira é uma lista de tuplos
turma = [
    (1, "Ana Costa", 16.4),
    (2, "Bruno Dias", 12.8),
    (3, "Carla Mendes", 17.9),
]
for numero, nome, media in turma:
    print(f"{numero:>2}  {nome:<14} {media:>5.1f}")

melhor = turma[0]
for aluno in turma:
    if aluno[2] > melhor[2]:
        melhor = aluno
print("Melhor média:", melhor[1])
