caneta = int(input("digite a quantidade de canetas compradas: "))
caderno = int(input("Digite a quantiadade de cadernos comprados: "))
lapis = int(input("Digite a quantidade de lapis comprados: "))

preco_canetas = float(input("Digite o preço de uma caneta: "))
preco_cadernos = float(input("Digite o preço de um caderno: "))
preco_lapis = float(input("Digite o preço de um lapis: "))

desconto_caneta = (caneta * preco_canetas) * 0.05
desconto_caderno = (caderno * preco_cadernos) * 0.20

total_compra = (lapis * preco_lapis) + desconto_caderno + desconto_caneta

print(f"O preço total da compra do material escolar foi de: R$ {total_compra:.2f}")