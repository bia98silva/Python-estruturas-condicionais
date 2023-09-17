custo_fabrica = float(input("Digite o custo de fabrica do carro: "))

percentual_distribuidor = 0.28
percentual_impostos =  0.45

custo_distribuidor = custo_fabrica * 0.28
custo_imposto = custo_fabrica * 0.45

custo_final = custo_fabrica + custo_distribuidor + custo_imposto

print(f"O custo do carro novo sera de R${custo_final:.2f}")