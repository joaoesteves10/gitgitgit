import math
import re

def pedirNums(requiredAmount = 0, minAmount = 1):
    """
    Obtem como input uma certa quantidade de números (requiredAmount, ilimitado se omitido ou zero), retornando uma lista dos valores
    Para terminar a entrada de valores, quando e apenas quando não existe requiredAmount, basta usar enter duas vezes seguidas
    """
    list = []
    emptyEnterCount = 0
    print("introduza os valores em que deseja operar, separados por linhas")
    if (requiredAmount != 0):
        print(f"são necessários exatamente {requiredAmount} valores")
    else:
        print(f"são necessários pelo menos {minAmount} valores; use enter duas vezes para terminar a entrada de dados")
    while True:
        if (requiredAmount != 0) and (len(list) == requiredAmount):
            return list
        num = input("> ").replace(",", ".")
        if num.isnumeric() or (len(re.findall("[.]", num)) <= 1 and re.sub("[.]", "", num).isnumeric()) or (num.startswith("-") and len(re.findall("[.]", num)) <= 1 and len(re.findall("[-]", num)) == 1 and re.sub("[-.]", "", num).isnumeric()): # se o valor for válido, adicioná-lo à lista
            list.append(float(num))
        elif (num == "" and requiredAmount == 0 and len(list) >= minAmount): # enter duas vezes para terminar a entrada de dados
            emptyEnterCount += 1
            if emptyEnterCount == 2:
                return(list)
            print("use enter novamente para terminar a entrada de dados")
        else:
            print("o valor introduzido é inválido, logo não foi adicionado à operação; tente novamente")
            continue

def somar(): # retorna a soma de dois ou mais números
    print("SOMAR")
    return(sum(pedirNums()))


def subtrair(): # retorna a diferença de dois ou mais números
    print("SUBTRAIR")
    diff = 0
    for i, num in enumerate(pedirNums()):
        if i == 0:
            diff = num
            continue
        diff -= num
    return (diff)


def multiplicar(): # retorna o produto de dois ou mais números
    print("MULTIPLICAR")
    prod = 0
    for i, num in enumerate(pedirNums()):
        if i == 0:
            prod = num
            continue
        prod *= num
    return (prod)

def dividir(): # retorna o quociente de dois ou mais números ou uma string de erro para tentativas de dividir por zero
    print("DIVIDIR")
    quo = 0
    list = pedirNums()
    for i, num in enumerate(list):
        if i == 0:
            quo = num
            continue
        if int(num) == 0:
            return(f"erro: não é possível dividir por zero {list}")
        quo /= num
    return (quo)

def fatorial(): # retorna o fatorial de um número
    print("FATORIAL")
    return(math.factorial(int(pedirNums(1)[0])))

def paridade(): # retorna a paridade de um número (par/impar)
    print("PARIDADE")
    if (pedirNums(1)[0] % 2 == 0 ):
        return "par"
    else:
        return "impar"

def raizQuadrada(): # retorna a raiz quadrada de um número ou uma string de erro para tentativas de obter a raiz de um número negativo
    print("RAIZ QUADRADA")
    num = pedirNums(1)[0]
    if str(num).startswith("-"):
            return(f"erro: não é possível obter a raiz de um número negativo [{num}]")
    return(math.sqrt(num))

def menu():

    menuDict = {
        "a": somar,
        "b": subtrair,
        "c": multiplicar,
        "d": dividir,
        "e": fatorial,
        "f": paridade,
        "g": raizQuadrada
        }

    while True:

        print("a: somar")
        print("b: subtrair")
        print("c: multiplicar")
        print("d: dividir")
        print("e: fatorial")
        print("f: par/impar")
        print("g: raiz quadrada")
        print("h: fechar")
        print("-----------------------")

        x = input("escolha uma operação:\n> ")
        if x == "h":
            print("sayonara 👋")
            exit()
        elif x in menuDict:
            print("-----------------------")
            result = menuDict[x]()
            print("-----------------------")
            print(result)
        else:
            print("-----------------------")
            print("operação inválida")

        print("-----------------------")

menu()
