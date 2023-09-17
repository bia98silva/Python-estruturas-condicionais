primeira_pessoa = input("Digite um nome: ")
altura_primeira_pessoa = float(input("Digite a altura da primeira pessoa: "))
segunda_pessoa = input("Digite o segundo nome: ")
altura_segunda_pessoa = float(input("Digite a altura da segunda pessoa:"))

if altura_primeira_pessoa > altura_segunda_pessoa:
    print(f"A pessoa mais alta é {primeira_pessoa} com uma altura de {altura_primeira_pessoa}")
else:
    print(f"A pessoa mais alta é {segunda_pessoa} com uma altura de {altura_primeira_pessoa}")