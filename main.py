#Desafio extra

aluno = ""

nota = 0

lista = []

conjunto = (aluno, nota)

ind = 1

while aluno != "0":
    print("Cadastro de alunos! Digite '0' para encerrar")

    aluno = input("Digite o nome de um aluno: ")

    nota = float(input("Digite a nota desse aluno: "))
    conjunto = (aluno, nota)
    lista.append(conjunto)

lista.remove(lista[-1])

for i in lista:
    if i[1] >= 7:
        print(f"Aluno {ind} ({i[0]}) tirou a nota: {i[1]}... Situação: APROVADO :)")
        ind += 1

    else:
        print(f"Aluno {ind} ({i[0]}) tirou a nota: {i[1]}... Situação: REAPROVADO :(")
        ind += 1








