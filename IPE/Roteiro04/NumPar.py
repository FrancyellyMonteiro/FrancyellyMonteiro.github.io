contador = 0

while contador == 5:
    num_user = int(input("digite um numero: "))
    
    if num_user%2 == 0:
        contador = contador + 1
    else:
        continue
