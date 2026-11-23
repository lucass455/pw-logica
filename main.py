#EXERCICIO 7

numero = int(input("Digite o número de notas: "))
soma = 0

for i in range(0, numero):
    nota = float(input("Digite a nota: "))
    soma += nota

media = soma / numero

print(f"Sua média é: {media:.2f}")
