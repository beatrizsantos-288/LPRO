"""Gestão de stock da loja: o menu que o utilizador vê."""
from datetime import date

import bd
import stock


def ler_inteiro(pergunta, minimo=None):
    """Pede um inteiro até o valor ser válido."""
    while True:
        texto = input(pergunta).strip()
        try:
            valor = int(texto)
        except ValueError:
            print(f"  '{texto}' não é um número inteiro.")
            continue
        if minimo is not None and valor < minimo:
            print(f"  Tem de ser pelo menos {minimo}.")
        else:
            return valor


def ler_preco(pergunta):
    """Aceita 12,50 ou 12.50."""
    while True:
        texto = input(pergunta).strip().replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("  Escreve um valor, por exemplo 12,50.")


def euros(valor):
    """1077.3 fica '1 077,30'."""
    texto = f"{valor:,.2f}"            # '1,077.30'
    return texto.replace(",", " ").replace(".", ",")


def listar():
    produtos = stock.listar_produtos()
    if not produtos:
        print("Ainda não há produtos.")
        return
    print(f"{'CÓDIGO':<8}{'PRODUTO':<15}{'QTD':>4}")
    for p in produtos:
        print(f"{p['codigo']:<8}{p['nome'][:14]:<15}{p['stock']:>4}")


def novo_produto():
    codigo = input("Código: ")
    nome = input("Nome: ")
    preco = ler_preco("Preço: ")
    minimo = ler_inteiro("Stock mínimo: ", minimo=0)
    stock.adicionar_produto(codigo, nome, preco, minimo)
    print("Produto criado com stock 0.")


def movimento(tipo):
    produto = stock.procurar(input("Código: "))
    if produto is None:
        print("Esse código não existe. Usa a opção 1.")
        return
    print(f"{produto['nome']}: stock {produto['stock']}")
    quantidade = ler_inteiro("Quantidade: ", minimo=1)
    nota = input("Nota (pode ficar vazia): ").strip()
    novo = stock.registar_movimento(
        produto["codigo"], tipo, quantidade, nota)
    print(f"Registado. Stock agora: {novo}")


def alertas():
    lista = stock.em_falta()
    if not lista:
        print("Nenhum produto abaixo do mínimo.")
    for p in lista:
        print(f"{p['codigo']:<8} tem {p['stock']}, mínimo {p['minimo']}")


def historico():
    codigo = input("Código: ")
    linhas = stock.movimentos(codigo)
    if not linhas:
        print("Sem movimentos para esse código.")
    for m in linhas:
        sinal = "+" if m["tipo"] == "entrada" else "-"
        qtd = f"{sinal}{m['quantidade']}"
        print(f"{m['data']} {qtd:>4} {m['nota']}")


def mostrar_relatorio():
    linhas, total = stock.relatorio()
    baixo = 0
    print("RELATÓRIO DE STOCK")
    print(f"{date.today():%d/%m/%Y} · {len(linhas)} produtos")
    print("=" * 25)
    print(f"{'PRODUTO':<13}{'QTD':>4}{'VALOR €':>8}")
    for p in linhas:
        alerta = ""
        if p["stock"] <= p["minimo"]:
            alerta = " !"
            baixo += 1
        print(f"{p['nome'][:13]:<13}{p['stock']:>4}"
              f"{euros(p['valor']):>8}{alerta}")
    print("=" * 25)
    print(f"{'TOTAL':<17}{euros(total):>8}")
    print(f"! abaixo do mínimo: {baixo}")


def main():
    bd.criar_tabelas()
    if stock.carregar_exemplo():
        print("Loja nova: 5 produtos de exemplo.")
    while True:
        print("\n===== GESTÃO DE STOCK =====")
        print("1 Listar     2 Novo produto")
        print("3 Entrada    4 Saída")
        print("5 Em falta   6 Histórico")
        print("7 Relatório  0 Sair")
        opcao = input("Opção: ").strip()
        try:
            if opcao == "1":
                listar()
            elif opcao == "2":
                novo_produto()
            elif opcao == "3":
                movimento("entrada")
            elif opcao == "4":
                movimento("saida")
            elif opcao == "5":
                alertas()
            elif opcao == "6":
                historico()
            elif opcao == "7":
                mostrar_relatorio()
            elif opcao == "0":
                print("Até amanhã!")
                break
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print("Não foi possível:", erro)


if __name__ == "__main__":
    main()
