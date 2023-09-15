inicio = int(input("Digite o inicio do intervalo: "))
fim = int(input("Digite o final do intervalo: "))

soma_pares = 0
soma_impares = 0

for i in range(inicio,fim+1):
    if i % 2 == 0:
        soma_pares += i
    else:
        soma_impares += i
print(f"A soma dos pares no intervalo de {inicio} e {fim} é de: {soma_pares}")
print(f"A soma dos pares no intervalo de {inicio} e {fim} é de: {soma_impares}")

