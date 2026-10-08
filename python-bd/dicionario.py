"""Exemplo de Dicionário que permite guardar dados do produto e 
aceder valores através das chaves"""

produto = {"codigo": "RATO-01", "nome": "Rato sem fios", "stock": 12}
print(produto["nome"])

produto["preco"] = 14.9            # acrescenta uma chave
produto["stock"] -= 2              # altera um valor
print(produto.get("cor", "sem cor"))  # valor por omissão

for chave, valor in produto.items():
    print(f"{chave:>7}: {valor}")
