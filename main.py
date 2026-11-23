#EXERCICIO 10


soma = 0

while True:
    print("Digite '1' para digitar o preço de um produto, '0' para encerrar")

    op = input("Digite uma opção: ")

    if op == "1":
        print("ADICIONAR PREÇO")
        preco = float(input("Digite o preço do produto que quer adicionar: "))
        soma = soma + preco

    elif op == "0":
        print(f"a soma total dos preços é: {soma:.2f}")
        break

