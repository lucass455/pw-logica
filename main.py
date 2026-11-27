#EXERCICIO 6

encontrado = False

produtos = ["Mouse", "Teclado", "Monitor", "Headset", "Webcam"]
print(produtos)


while encontrado == False:

    remover = input("Digite um produto para remover: ")

    if remover in produtos:
        produtos.remove(remover)
        print("Produto removido!")
        encontrado = True

    else:
        print("Produto não encontrado")



print(produtos)