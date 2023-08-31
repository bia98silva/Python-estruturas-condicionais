ano = int(input("Digite um ano (1000-2999): "))


if 1000 <= ano <= 2999:

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")
else:
    print("Ano fora da faixa válida (1000-2999).")