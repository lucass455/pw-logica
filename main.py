#EXERCICIO 5

senha = "lucas12345"

while True:
    tentativa = input("Digite a senha: ")
    
    if tentativa == senha:
        print("Acesso permitido!")
        break

    else:
        print("senha incorreta, tente novamente")
