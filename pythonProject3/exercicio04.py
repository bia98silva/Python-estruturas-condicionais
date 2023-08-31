qtd_macas = int(input("Digite a quantidade de maças compradas: "))

if qtd_macas >= 12:
    custo = qtd_macas * 1.00
    print(f"O custo total da compra foi de: R${custo: .2f}")
else:
    custo2 = qtd_macas * 1.30
    print(f"O custo total da compra foi de: R${custo2: .2f}")
