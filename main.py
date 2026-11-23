#EXERCICIO 9

import random

print("=== JOGO DE ADVINHAÇÃO ===")

numero = random.randint(1, 20)

while True:

    tentativa = int(input("Tente acertar o número: "))

    if tentativa < numero:
        print("O número secreto é MAIOR!")


    elif tentativa > numero:
        print("O número secreto é MENOR!")

    
    elif tentativa == numero:
        print("Parabéns! Você acertou o numero!!!!!!!!!!!!!!")
        break

