nome_empresa = input("Digite o nome da empresa: ")

soma_salario = 0

for i in range(5):
    nome = input("Digite o nome do funcionario: ")
    salario = float(input("Digite o salario do funcionario: "))
    soma_salario += salario
    if i == 0: # primeira leitura das variaveis
        maior_salario = salario
        nome_maior_salario = nome
        menor_salario = salario
        nome_menor_salario = nome
    else:  # leitura do segundo salario pra frente
        if salario > maior_salario:
            maior_salario = salario
            nome_maior_salario = nome
        if salario < menor_salario:
            menor_salario = salario
            nome_menor_salario = nome

media_salario = soma_salario / 5

print(f"A media salarial dos funcionarios da empresa {nome_empresa} é: R${media_salario:.2f}")
print(f"O funcionario com o maior salario é o: {nome_maior_salario} com um salario de: R${maior_salario:.2f}")
print(f"O funcionario que recebe o menor salario é o: {nome_menor_salario} com um salario de: R${menor_salario:.2f}")





