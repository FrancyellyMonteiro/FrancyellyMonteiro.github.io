lado01 = int(input("digite o tamanho do primeiro lado: "))
lado02 = int(input("digite o tamanho do segundo lado: "))
lado03 = int(input("digite o tamanho do terceiro lado: "))

if lado01 == lado02 and lado02 == lado03 and lado01 == lado03:
    print ("Possui três lados iguais portanto é um TRIÂNGULO EQUILATERO")
elif lado01 == lado02 != lado03 or lado02 == lado03 != lado01 or lado01 == lado03 != lado02:
    print ("Possui três lados iguais portanto é um TRIÂNGULO ISÓSCELES")
else:
    print("Não possui nenhum lado igual portanto é um TRIÂNGULO ESCALENO")