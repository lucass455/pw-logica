#EXERCICIO 12

print("=== MENU DE OPERAÇÕES ===")

op = ""

while op != "4":

    print("1- Mostrar uma mensagem de boas-vindas")
    print("2- Mostrar a tabuada de um número informado")
    print("3- Informar se um número é par ou ímpar")
    print("4- Sair")

    op = input("Digite a opção: ")

    if op == "1":
        print("Boas-vindas!")

    elif op == "2":
        num = int(input("Digite um número: "))
        contador = 1

        for i in range(0, 10):
            print(num * contador)
            contador += 1

    elif op == "3":
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print(f"O número: {numero} é par!")

        else:
            print(f"O número: {numero} é ímpar!")

    elif op == "4":
        break


    else:
        print("Digite uma opção válida!")

