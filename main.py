#EXERCICIO 4

num = int(input("Digite um número: "))
soma = 0
contador = 1

if num > 0:

    for i in range(0, num):
        soma += contador
        contador += 1
    print(soma)

else:
    print("digite um numero positivo")