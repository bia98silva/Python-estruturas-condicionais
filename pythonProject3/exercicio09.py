peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = peso / (altura ** 2)

if imc <= 18.5:
    situacao = "Abaixo do peso"
elif 18.5 < imc <= 24.9:
    situacao = "Peso ideal"
else:
    situacao = "Acima do peso"

print(f"O IMC calculado é: {imc:.2f}")
print(f"Situação: {situacao}")
