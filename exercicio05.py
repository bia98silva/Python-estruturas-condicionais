n = int(input("Digite o numero do fatorial que deseja: "))
fat = 1

for i in range(1,n+1):
    fat = fat * i
print(f"O fatorial de n é: {fat}")

