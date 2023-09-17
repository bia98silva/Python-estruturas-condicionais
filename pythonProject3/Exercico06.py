nome = input("Digite o nome do funcionário: ")
salario_bruto = float(input("Digite o salário bruto do funcionário: R$ "))


if salario_bruto <= 1100.0:
    desconto_inss = salario_bruto * 0.075
elif salario_bruto > 1100.0 and salario_bruto <= 2203.48:
    desconto_inss = salario_bruto * 0.09
elif salario_bruto > 2203.48 and salario_bruto <= 3305.22:
    desconto_inss = salario_bruto * 0.12
else:
    desconto_inss = salario_bruto * 0.14


print(f"O valor do desconto do INSS para o(a) funcionário(a) {nome} é: R$ {desconto_inss:.2f}")