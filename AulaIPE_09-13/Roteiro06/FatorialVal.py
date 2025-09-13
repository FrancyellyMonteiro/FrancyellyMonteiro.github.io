n = int(input("Digite um número inteiro: "))

def fatorial(n: int) -> int:

    if n < 0: 
        return 'O número deve ser positivo'

    res = 1
    for i in range (1, n+1):
        res = res*i
    return res