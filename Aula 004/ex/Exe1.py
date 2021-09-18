def somar(num1, num2):
    resultado = num1 + num2

    print("o resultado é", resultado)

def receberinputdousuário():
    num1 = int(input("insira o primeiro número"))
    num2 = int(input("insira o segundo número"))

    somar(num1, num2)

receberinputdousuário()