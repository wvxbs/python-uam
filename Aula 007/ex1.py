def ReceiveUserInput(Message):
    Input = int(input(f"{Message}:  "))

    return Input

def VerifyIfNumberIsValid(Number):
    if(Operation(Number) == 0):
        return False
    else:
        return True

def Operation(Number):
    Result = Number % 2

    return Result

def main():
    Counter = 0
    Acc = 0

    while(Counter < 5):
        Number = ReceiveUserInput(f"Insira o {1 + Counter} numero") 
        if(VerifyIfNumberIsValid(Number)):
            Acc = Number + Acc

        Counter = 1 + Counter

    print(f"A soma dos numeros impares é: {Acc}")    

main()