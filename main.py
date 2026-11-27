#EXERCICIO 7

op = ""

lista_alunos = []

while op != "5":
    print("=== CADASTRO DE ALUNOS ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Remover aluno")
    print("4 - Quantodade de alunos")
    print("5 - Sair")

    op = input("Digite uma opção: ")

    if op == "1":
        print("CADASTRAR ALUNO")
        adicionar_aluno = input("Digite o nome de um aluno para cadastrar: ")
        lista_alunos.append(adicionar_aluno)
        print("Aluno cadastrado!")

    elif op == "2":
        print("LISTAGEM DE ALUNOS")
        ind = 1
        for i in lista_alunos:
            print(f"Aluno {ind}: {i}")
            ind += 1

    elif op == "3":
        print("REMOVER ALUNO")
        remover_aluno = input("Digite o nome do aluno que quer remover: ")
        lista_alunos.remove(remover_aluno)
        print("Aluno removido!")
        
    elif op == "4":
        print("QUANTIDADE DE ALUNOS")
        print(f"O número de alunos é: {len(lista_alunos)}")

    elif op == "5":
        print("SAINDO...")
        break

    else:
        print("Digite uma opção válida!")

