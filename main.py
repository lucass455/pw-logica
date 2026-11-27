#EXERCICIO 4

notas = []

soma = 0

for i in range(5):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

print(f"As notas são: {notas}")

for nota in notas:
    soma = soma + nota

print(f"A soma das notas é: {soma:.1f}")

media = soma / 5

print(f"A média das notas é: {media:.2f}")

maior = max(notas)

print(f"A maior nota é: {maior}")

menor = min(notas)

print(f"A menor nota é: {menor}")


