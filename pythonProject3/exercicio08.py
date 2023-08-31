preco_livro = float(input("Digite o preço do livro: "))

if preco_livro > 60.00:
    desconto1 = preco_livro * 0.20
    preco_novo1 = preco_livro - desconto1
    print(f"O valor do livro com desconto será de: R${preco_novo1:.2f}")
elif 10.01 <= preco_livro <= 60.00:
    desconto2 = preco_livro * 0.1
    preco_novo2 = preco_livro - desconto2
    print(f"O valor do livro com desconto será de: R${preco_novo2:.2f}")
else:
    desconto3 = preco_livro * 0.08
    preco_novo3 = preco_livro - desconto3
    print(f"O valor do livro com desconto será de: R${preco_novo3:.2f}")
