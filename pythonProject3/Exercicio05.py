porcao_fritas = int(input("Dgite a quantidade de porcoes de fritas consumidas: "))
procao_pasteis = int(input("Digite a quantidade de procoes de pasteis consumidas: "))
qtd_cervejas = int(input("Digite a quantidade de cervejas consumidas: "))
amigos = int(input("Digite o total de pessoas: "))

total_pedido = (procao_pasteis * 25.00) + (porcao_fritas * 35.00) + (qtd_cervejas * 18.00)

valor_individual = total_pedido /amigos

print(f"O total do pedido foi de: R$ {total_pedido:.2f} e o valor individual para cada amigo ficou: R$ {valor_individual:.2f}")