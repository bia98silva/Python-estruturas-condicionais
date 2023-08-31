horas = int(input("Qual foi o periodo de permanência?"))
if horas >= 7:
    print("O total a pagar será de: R$ 35,00")
else:
    total_horas = horas * 5
    print(f"O total a pagar será de: {total_horas}")