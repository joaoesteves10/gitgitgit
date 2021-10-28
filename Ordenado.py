nomeAluno = input("Nome: ")
nota = int(input("Qual a nota que o aluno teve 0-200: "))

print("Nome: ", nomeAluno)
print("Nota: ", nota)


if (nota > 200 or nota < 0):
    print("Nota invalida")
elif (nota >= 95):
    print("O aluno passou")    
elif (nota < 95):
        print("O aluno reprovou")
else:
    print("Nota invalida")

