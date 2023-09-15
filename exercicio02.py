num1 = int(input("Digite um numero para o inicio do intervalo: "))
num2 = int(input("Digite o final do intervalo:"))
pares = 0
impares = 0

for i in range(num1, num2 + 1):
     if i % 2 == 0:
          pares += 1
     else:
          impares +=1
print(f"A quantidade de numeros pares é: {pares}")
print(f"A quantidade de numeros impares é: {impares}")
