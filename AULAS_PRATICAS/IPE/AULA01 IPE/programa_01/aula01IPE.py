nome = 'Francyelly'
idade = 19
cidade = 'Sumare'
profissao = 'Analista de Dados'
# Foi criada 4 variáveis para adquirir os valores de nome, idade, cidade e profissão que iremos utilizar
# ao executarmos os próximos comandos no terminal.

print(nome)
print(idade)
print(cidade)
print(profissao)
# O print() é utilizado para exibir informações no terminal. Nesse caso estamos o utilizando para exibir os 
# valores atribuídos as variáveis nome, idade, cidade e profissão.

print(f"Olá meu nome é {nome}, tenho {idade} anos, moro em {cidade} e sou {profissao}")
# O f-string utilizado no começo da frase é uma forma pratica de conseguir inserir variáveis dentro de uma string.
# Com isso, como estamos adicionando as variáveis nome, idade, cidade e profissão (localizadas dentro das chaves)
# na frase digitada acima, adicionamos o f-string para que elas sejam incorporadas na informação exibida no terminal.

print("Tenho {0:3d} anos".format(idade))
# O .format() utilizado no comando acima tem a função de formatar strings que serão exibidas no terminal.
# Nesse caso, ao invés de colocarmos o nome da variável dentre chaves no meio da frase, iremos adicionar certos
# parâmetros que será interpretado pelo .format(). O número 0 dentre chaves indica que será usado o primeiro 
# argumento passado para o método .format(), nesse caso será a variável idade, o :3d significa que o número guardado
# dentro da variável idade irá ocupar pelo menos 3 espaços na linha e que ele é um número decimal inteiro. 
# Finalizando o comando, o .format(idade) tem a função de passar o valor da variável idade para substituir {0} na 
# string.

print(nome, cidade, sep=" - ")
# O sep="" tem a função de adicionar um separador nas variáveis a serem exibidas. Com isso, ao código ser executado
# e exibido no terminal, as variáveis nome e cidade terão um traço (-) dentre elas para separa-las.
