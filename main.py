#EXERCICIO 8

preco = 1

lista_precos = []

ind = 0

while preco != 0.0:
    preco = float(input("Digite um preço para adicionar, digite '0' caso queira parar: "))
    lista_precos.append(preco)
    ind += 1

lista_precos.remove(0.0)

print(lista_precos)

soma = 0

for i in lista_precos:
    soma = soma + i

print(f"O total da compra é: {soma}")

print(f"O total de itens é: {ind - 1}")

media = soma / ind


print(f"O preço médio é: {media}")

    


