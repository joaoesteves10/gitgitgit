ordenado = int(input("Qual o seu ordenado: "))

if (0 < ordenado <= 1000):
    aumento = 0.07
elif (ordenado > 1000):
    aumento = 0.05
else:
    print("ERRO")
    exit()

novoOrdenado = ordenado + ordenado * aumento

print("o seu ordenado com o aumento é: ", novoOrdenado)
