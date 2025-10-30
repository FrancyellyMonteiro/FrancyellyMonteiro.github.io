nome = input ('Digite seu nome: ')
idade = input ('Digite sua idade: ')
cor = input ('Informe sua cor favorita: ')
# Foram criadas três variáveis chamadas nome, idade e cor. Ao invés de darmos os valores atribuídos a essas
# variáveis adicionamos o input(). Ele terá a função de exibir a frase escrita dentre parênteses no terminal 
# quando executado e armazenar o valor inserido pelo usuário dentro das variáveis acima.

print(nome)
print(idade)
print(cor)
# Irá exibir o valor inserido nas variáveis nome, idade e cor.

print(f'Que legal, {nome}! \nEntão você tem \t {idade} anos \ne adora a cor \t{cor}')
# Os comandos \n e \t tem a função de quebra de linha e tab respectivamente.
# O print irá exibir a frase escrita conforme parâmetros adicionados.

print(nome, idade, cor, sep="* *")
# Irá exibir no terminal os valores das variáveis nome idade e cor com o separador (-) dentre elas.
