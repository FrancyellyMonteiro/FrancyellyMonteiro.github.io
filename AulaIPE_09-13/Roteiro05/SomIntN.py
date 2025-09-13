limite = int(input("Digite um numero inteiro positivo: "))
resposta = 0

if limite > 0:
    for n in range(limite+1):
        resposta = resposta+n
        print(resposta)
else:
    print("O numero que vc digitou não é um numero inteiro positivo")
