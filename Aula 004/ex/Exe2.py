def ExibirResultado(Mensagem, Resultado):
    print(Mensagem, ": ", Resultado)

def ReceberInputDoUsuario(Mensagem):
    Entrada = float(input(Mensagem))

    return Entrada

def CalcularMedia(Nota1, Nota2, Nota3):

    media = (Nota1 + Nota2 + Nota3) / 3

    return media

def main():
    Nota1 = ReceberInputDoUsuario("Insira a primeira nota")
    Nota2 = ReceberInputDoUsuario("Insira a segunda nota")
    Nota3 = ReceberInputDoUsuario("Insira a terceira nota")

    resultado = CalcularMedia(Nota1, Nota2, Nota3)

    ExibirResultado("A média das notas é", resultado) 

main()