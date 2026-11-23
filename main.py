#EXERCICIO 1
# idade = input("Digite sua idade: ")

# if idade >= 18:
#     print("Você é maior de idade!")




# EXERCICIO 2
# idade = input("Digite sua idade: ")

# if idade >= 18:
#     print("Você é maior de idade!")

# else:
#     print("Você é menor de idade")




#EXERCICIO 3
# nota = float(input("Digite sua nota: "))

# if nota == 10:
#     print(True)

# else:
#     print(False)


# if nota != 0:
#     print(True)

# else:
#     print(False)


# if nota >= 7:
#     print("True")

# else:
#     print(False)





#EXERCICIO 4

# nota = float(input("Digite sua nota: "))

# if nota >= 9:
#     print("Conceito A - Excelente!")

# elif 9 > nota >= 7:
#     print("Conceito B - Bom!")

# elif 7 > nota >= 5:
#     print("Conceito C - Regular")

# else:
#     print("Reprovado :(")





#EXERCICIO 5
# nome = input("Digite seu nome: ")
# peso = float(input("Digite seu peso (kg): "))
# altura = float(input("Digite sua altura (m): "))

# IMC = peso / (altura ** 2)

# print(f"Olá {nome}! seu IMC é {IMC:.1f}!")

# if IMC < 18.5:
#     print("Abaixo do peso")

# elif 18.5 < IMC < 25:
#     print("Peso normal")

# elif 30 < IMC < 25:
#     print("Sobrepeso")

# else:
#     print("Obesidade")





#EXERCICIO 6
# n1 = float(input("Digite o primeiro número: \n"))
# n2 = float(input("Digite o segundo número: \n"))

# operação = input("Digite a operação \n '+' para somar \n '-' para diminuir \n '*' para multiplicar \n '/' para dividir \n Digite: ")

# if n1 != 0:
#     if n2 != 0:

#         if operação == "+":
#             print(f"{n1} + {n2} = {n1 + n2}")

#         elif operação == "-":
#             print(f"{n1} - {n2} = {n1 - n2}")

#         elif operação == "*":
#             print(f"{n1} * {n2} = {n1 * n2:.2f}")

#         elif operação == "/":
#             print(f"{n1} / {n2} = {n1 / n2:.2f}")


#     else:
#         print("Erro! Não pode dividir por zero!")
# else:
#     print("Erro! Não pode dividir por zero!")






#EXERCICIO 7
# import random

# escolhas = ["pedra", "papel", "tesoura"]

# jogada_player = input("Jogue: 'pedra', 'papel' ou 'tesoura': ").lower()

# jogada_robo = random.choice(escolhas)

# if jogada_player == "pedra":

#     if jogada_robo == "pedra":
#         print("Empate")

#     elif jogada_robo == "tesoura":
#         print("Vitória")

#     elif jogada_robo == "papel":
#         print("Derrota")



# elif jogada_player == "tesoura":

#     if jogada_robo == "tesoura":
#         print("Empate")

#     elif jogada_robo == "papel":
#         print("Vitória")

#     elif jogada_robo == "pedra":
#         print("Derrota")



# elif jogada_player == "papel":


#     if jogada_robo == "papel":
#         print("Empate")

#     elif jogada_robo == "pedra":
#         print("Vitória")

#     elif jogada_robo == "tesoura":
#         print("Derrota")


# else:
#     print("Jogue algo que funcione")






#EXERCICIO 8
# idade = int(input("Digite sua idade: "))

# if idade <= 0:
#     print("Idade inválida!")

# elif 0 < idade <= 12:
#     print("Criança")

# elif 12 < idade <= 17:
#     print("Adolescente")

# elif 17 < idade <= 59:
#     print("Adulto")

# elif idade >= 60:
#     print("Idoso")

# else:
#     print("Digite algo que fucnione por favor")




# EXERCICIO 9
# n1 = input("Jogador 1, digite seu nome: ")
# n2 = input("Jogador 2, digite seu nome: ")
# escolha = input(f"{n1}, par ou impar? ").lower()

# if escolha == "par":
#     jogador1 = int(input(f"{n1}, digite o seu número: "))
#     jogador2 = int(input(f"{n2}, voce é impar, digite o seu número: "))

#     jogada = jogador1 + jogador2

#     if jogada % 2 == 0:
#         print(f"Resultado: {jogada}, o {n1} venceu!")
    
#     else:
#         print(f"Resultado: {jogada}, o {n2} venceu!")


# elif escolha == "impar":
#     jogador1 = int(input(f"{n1}, digite o seu número: "))
#     jogador2 = int(input(f"{n2}, voce é par digite o seu número: "))

#     jogada = jogador1 + jogador2
    
#     if jogada % 2 == 0:
#         print(f"Resultado: {jogada}, o {n2} venceu!")
    
#     else:
#         print(f"Resultado: {jogada}, o {n1} venceu!")




#EXERCICIO 10
# ingresso = 40
# meia_entrada = False
# meia_entrada_estudante = False
# promo_quarta = False
# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# dia = input("Que dia é hoje?\n seg\n ter\n qua\n qui\n sex\n sab\n dom\n Digite: ")

# if dia == "qua":
#     promo_quarta = True


# if idade <= 12 or idade >= 60:
#     meia_entrada = True

# elif 12 < idade < 21:
#     estudante = input("Você tem carteirinha de estudante? (s/n)")
#     if estudante == "s":
#         meia_entrada_estudante = True
#     else:
#         pass


# print("=== CHECKOUT ===")

# if meia_entrada == True:
#     ingresso = ingresso - (ingresso / 2)
#     print("Promoção meia-entrada!")
#     if promo_quarta == True:
#         ingresso = ingresso - (ingresso / 2)
#         print("Promoção de quarta!")
#         print(f"{nome}, o valor ficou R$ {ingresso}")
#     else:
#         print(f"{nome}, o valor ficou R$ {ingresso}")

# elif meia_entrada_estudante == True:
#     ingresso = ingresso - (ingresso / 2)
#     print("Promoção estudante!")
#     if promo_quarta == True:
#         ingresso = ingresso - (ingresso / 2)
#         print("Promoção de quarta!")
#         print(f"{nome}, o valor ficou R$ {ingresso}")
#     else:
#         print(f"{nome}, o valor ficou R$ {ingresso}")

# elif promo_quarta == True:
#     ingresso = ingresso - (ingresso / 2)
#     print("Promoção de quarta!")
#     print(f"{nome}, o valor ficou R$ {ingresso}")

# else:
#     print(f"{nome}, o valor ficou R$ {ingresso}")




#EXERCICIO 11
# a = int(input("Digite o primeiro lado: "))
# b = int(input("Digite o segundo lado: "))
# c = int(input("Digite o terceiro lado: "))
# forma = False

# if (a < b + c) and (b < a + c) and (c < a + b):
#     print("Forma um triângulo!")
#     forma = True
    

# else:
#     print("Não forma um triângulo")
#     forma = False

# if forma == True:
#     if a == b == c:
#         print("Equilátero!")

#     elif a == b != c or a != b == c or a == c != b:
#         print("Isóceles!")

#     elif a != b != c:
#         print("Escaleno!")
    





#EXERCICIO 12
# def Celsius_para_Fahrenheit():
#     celsius = float(input("Digite a quantidade em celsius: "))
#     fahrenheit = (celsius * 1.8) + 32
#     print(f"{celsius} celsius = {fahrenheit:.2f} fahrenheits")


    
# def Quilômetros_para_Milhas():
#     km = float(input("Distância em km: "))
#     milhas = km / 1.609
#     print(f"{km} km = {milhas:.2f} milhas")

    
# def Reais_para_Dólar():
#     real = float(input("Quantidade em reais: "))
#     dolar = real / 5.78
#     print(f"{real} reais = {dolar:.2f} dólares")


    
# def Quilogramas_para_Libras():
#     kg = float(input("Quantidade em kg: "))
#     libras = kg * 2.20462262
#     print(f"{kg} km = {libras:.2f} libras")


# op = ""

# while op != "5":
#     print("1- Celsius para Fahrenheit")
#     print("2- Quilômetros para Milhas")
#     print("3- Reais para Dólar")
#     print("4- Quilogramas para Libras")
#     print("5- Sair")

#     op = input("Digite uma opção: ")

#     if op == "1":
#         Celsius_para_Fahrenheit()

#     elif op == "2":
#         Quilômetros_para_Milhas()

#     elif op == "3":
#         Reais_para_Dólar()

#     elif op == "4":
#         Quilogramas_para_Libras()

#     elif op == "5":
#         break

#     else:
#         print("Digite alguma opção que funcione")






#EXERCICIO 13
senha = "python123"
entrar = False


T_1 = input("Digite a senha: ")
while entrar != True:
    if T_1 == senha:
        print("Cofre aberto")
        print("Você tem R$ 1.000.000!")
        entrar = True

    elif T_1 != senha:
        print("senha errada, você tem mais 2 tentativas")
        T_1 = input("Digite a senha: ")

        if T_1 == senha:
            print("Cofre aberto")
            print("Você tem R$ 1.000.000!")
            entrar = True

        elif T_1 != senha:
            print("senha errada, você tem mais 1 tentativas")
            T_1 = input("Digite a senha: ")

            if T_1 == senha:
                print("Cofre aberto! Ufa, por pouco")
                print("Você tem R$ 1.000.000!")
                entrar = True

            elif T_1 != senha:
                print("BLOQUEADO! Chamando a polícia...")
                break




        



