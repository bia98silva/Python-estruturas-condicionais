num_tab = int(input("Digite um numero da tabuada que deseja: "))

for cont in range(11):
    tab = num_tab * cont
    print(f"{num_tab} X {cont} = {tab}")
