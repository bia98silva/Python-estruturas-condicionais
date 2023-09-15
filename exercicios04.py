taxa = float(input("Digite a taxa de abatimento: "))
qtd_prestacoes = int(input("Digite a quantidade de prestaçoes: "))
valor_primeira_prestacao = float(input("Digite o valor da primeira prestação: "))

for prest in range(qtd_prestacoes):
    if prest == 0:
        print(f"Prestação {prest+1}: {valor_primeira_prestacao:.2f}")
        valor_prest = valor_primeira_prestacao
    else:
        valor_prest = valor_prest - (valor_prest * taxa/100)
        print(f"Prestação {prest+1}: {valor_prest:.2f}")
