salario = float(input("Insira o salário:"))


if salario <= 600.00:
    print("isento")

elif 600.00 < salario >= 1200.00:
    print("20%")

elif 1200.00 < salario >= 2000.00:
    print("25%")

elif 2000.00 < salario:
    print("30%")

else:
    print("informação inválida")