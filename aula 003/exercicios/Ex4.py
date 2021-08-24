idade = int(input("Insira a idade do nadador:"))


if idade < 5:
    print("categoria: bebê")

elif 5 <= idade >= 7:
    print("categoria: infantil A")

elif 8 <= idade >= 10:
    print("categoria: infantil B")

elif 11 <= idade >= 13:
    print("categoria: juvenil A")

elif 14 <= idade >= 17:
    print("categoria: juvenil B")

elif idade >= 18:
    print("categoria: Sênior")

else:
    print("informação inválida")