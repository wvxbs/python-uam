idade = int(input("Digite a idade do trabalhador"))
tempoServico = int(input("Digite o tempo de serviço do trabalhador"))

if idade > 66:
    print("a pessoa pode se aposentar")

elif tempoServico >31:
    print("a pessoa pode se aposentar")

elif idade > 61 and tempoServico > 26:
    print("a pessoa pode se aposentar")

else:
    print("a pessoa não pode se aposentar")