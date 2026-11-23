#EXERCICIO 6

senha = "lucas12345"
contagem_T = 0

while True:
    tentativa = input("Digite a senha: ")
    
    if tentativa == senha:
        print("Bem-vindo!")
        break

    else:
        print("senha incorreta, tente novamente")
        contagem_T += 1
        if contagem_T == 3:
            print("Conta bloqueada")
