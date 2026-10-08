"""Exemplo de Lista de alunos, que permite adicionar, remover, ordenar e 
pecorrer a lista utilizando o ciclo for """

alunos = ["Ana", "Bruno", "Carla"]

alunos.append("Diogo")
print(alunos[0], alunos[-1])
print(len(alunos), "alunos")

alunos.remove("Bruno")
print("Bruno" in alunos)

alunos.sort(reverse=True)
print(alunos)

for posicao, nome in enumerate(alunos, start=1):
    print(posicao, nome)