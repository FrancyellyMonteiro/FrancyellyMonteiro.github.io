senha = 123
contador = 0

while True:
    senha_user = input("digite sua senha: ")

    if senha == senha_user:
        print("senha correta")
        break
    else:
        contador = contador + 1 
        print(contador)  
        print(f"tentativa {contador} de 3")
        print("senha incorreta, digite novamente")
