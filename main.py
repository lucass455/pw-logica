#EXERCICIO 11

numero = int(input("Digite um numero positivo: "))
pares = 0
impares = 0

if numero >= 1:
    

    for i in range(0, numero):
        if i % 2 == 0:
            pares += 1

        else:
            impares += 1


else:
    print("Digite um numero positivo")


print(f"pares: {pares}")
print(f"impares: {impares}")


