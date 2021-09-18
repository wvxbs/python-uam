def fibonacci(n: int) -> int:

    if n <= 1:
        return n                                                                                                                                                                                                                                                                         
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    i = 1
    soma = 0

    while i <= 10000:           
        print(fibonacci(i))

        soma = soma + fibonacci(i)

        i = i + 1

    print("a soma da sequencia é: ", soma)

main()                                                     b