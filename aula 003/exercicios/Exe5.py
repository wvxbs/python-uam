numero1 = int(input("Digite o primeiro número"))
sinal = input("Digite o sinal: = - / *")
numero2 = int(input("Digite o segundo número"))

if sinal == "+":
    print(numero1 + numero2)

if sinal == "-":
    print(numero1 - numero2)

if sinal == "/":
    print(numero1 / numero2)

if sinal == "*":
    print(numero1 * numero2)

else:
    print("operação invalida")