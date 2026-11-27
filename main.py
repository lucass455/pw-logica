#EXERCICIO 5

numeros = []
pares = 0
impares = 0

for i in range(10):
    num = int(input("Digite um numero: "))
    numeros.append(num)

for i in numeros:
    if i % 2 == 0:
        print(f"O numero {i} é par")
        pares += 1
    
    else:
        print(f"O numero {i} é ímpar")
        impares += 1

print(f"A quantidade de números pares é: {pares}")
print(f"A quantidade de números ímpares é: {impares}")
