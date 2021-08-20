verdadeiro = 15
executar = True
palpite = 0

while executar:
    palpite = int(input("Insira o palpite"))

    if palpite == verdadeiro:
        print("acertou")
        executar = False

    elif palpite > verdadeiro:
        print("o número é menor que seu palpite")

    elif palpite < verdadeiro:
        print("o numer é maior que o seu palpite")
