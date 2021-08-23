numero1 = int(input("Digite o primeiro número"))
numero2 = int(input("Digite o segundo número"))

if numero1 == numero2:
    print(f"os numeros", numero1,"e", numero2, "são iguais")

elif numero1 < numero2:
    print(f"o número 1: {numero1} é menor que o número 2: {numero2}")

else:
    print(f"o número 2: {numero2} é menor que o número 1: {numero1}")