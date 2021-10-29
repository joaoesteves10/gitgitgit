import math

def pedirNums():
    list = []
    enterCount = 0
    while True:
        print("introduza os números em que deseja operar, separados por linha (dois enters para terminar): ")
        num = input("> ")
        if num.isnumeric():
            list.append(num)
        elif num == "":
            enterCount += 1
            if enterCount == 2:
                return list
        else:
            "o valor introduzido é inválido, não foi adicionado à operação"
            continue

def pedirDoisNum():
    while True:
        num1 = input("Digite o primeiro valor: ")
        num2 = input("Digite o segundo valor: ")

        if not (num1.isnumeric() and num2.isnumeric()):
            print("os valores introduzidos são inválidos")
            continue
        else:
            return int(num1), int(num2)

def pedirUmNum():
    while True:
        num = input("Digite um valor: ")

        if not (num.isnumeric()):
            print("O valor introduzido é inválido")
            continue
        else:
            return int(num)

def somar(): # retorna a soma de dois números
    num1, num2 = pedirDoisNum()
    return (num1 + num2)

def subtrair(): # retorna a diferença de dois números
    num1, num2 = pedirDoisNum()
    return (num1 - num2)

def multiplicar(): # retorna o produto de dois números
    num1, num2 = pedirDoisNum()
    return (num1 * num2)

def dividir(): # retorna o quociente de dois números
    num1, num2 = pedirDoisNum()
    """
    IMPLEMENTAR VERIFICAÇÃO PARA TENTATIVAS DE DIVIDIR POR ZERO
    """
    return (num1 / num2)

def fatorial(): # retorna o fatorial de um número
    num = pedirUmNum()
    math.factorial(num)

def paridade(): # retorna a paridade de um número (par/impar)
    num = pedirUmNum()
    if (num % 2 == 0 ):
        return "par"
    else:
        return "impar"

def raizQuadrada(): # retorna a raiz quadrada de um número
    num = pedirUmNum()
    return(math.sqrt(num))



def menu():
    print("-----------------------")
    print("1: somar")
    print("2: subtrair")
    print("3: multiplicar")
    print("4: dividir")
    print("5: fatorial")
    print("6: par/impar")
    print("7: raiz quadrada")
    print("8: fechar")
    print("-----------------------")

    while True:
        x = input("escolha uma operação: ")
        if x == "1":
            print(somar())
        elif x == "2":
            print(subtrair())
        elif x == "3":
            print(multiplicar())
        elif x == "4":
            print(dividir())
        elif x == "5":
            print(fatorial())
        elif x == "6":
            print(paridade())
        elif x == "7":
            print(raizQuadrada())
        elif x == "8":
            print("sayonara 👋")
            exit()
        else:
            print("operação inválida")

menu()
