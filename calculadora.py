print("Insira o primeiro número:")
numA = input()

print("Insira o segundo numero:")
numB= input()

operador = "Escolha a operação: {}, {}, {}, {}, {}")
print(operador("+","-","x","/", "%"))
operador= input()

try:
    if(variavel_operador == "+"):
        print(numA + numB)
    else if(variavel_operador == "*"):
        print(numA * numB)
    else if(variavel_operador == "-"):
        print(numA - numB)
    else if(variavel_operador == "/"):
        print(numA / numB)
    else if(variavel_operador == "%"):
        print(numA % numB)
    else:
        print("ERRO: operação inválida")
expect Exception as err:
        print("ERRO: " + err.error())
