num = int(input("Digite um numero: "))
isPrimo = True

for i in range(2, num):
    if num % i == 0:
        isPrimo = False
    break

if isPrimo:
    print(f'o numero {num} é primo')
else:
    print(f'o numero {num} não é primo')