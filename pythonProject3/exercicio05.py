media_anual = float(input("Digite a média anual do aluno: "))


if media_anual >= 6.0:
    print("Aluno aprovado!")
elif 3.0 <= media_anual < 6.0:
    print("Aluno de exame.")
else:
    print("Aluno reprovado.")