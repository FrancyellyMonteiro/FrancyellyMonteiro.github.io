from datetime import date
data_atual = date.today()
ano_atual = data_atual.year
mes_atual = data_atual.month
dia_atual = data_atual.day

dia_nasc = int(input("Digite o dia do seu nascimento: "))
mes_nasc = int(input("Digite o mês do seu nascimento: "))
ano_nasc = int(input("Digite o ano do seu nascimento: "))

dif_ano = ano_atual - ano_nasc
dif_mes = mes_atual - mes_nasc
dif_dia = dia_atual - dia_nasc

if dif_ano > 18:
    print("Sim, você já pode tirar sua CNH")
elif dif_ano < 18:
    print("Não, você ainda não pode tirar sua CNH")
else:

    if dif_mes > 0:
        print("Sim, você já pode tirar sua CNH")
    elif dif_mes < 0:
        print("Não, você ainda não pode tirar sua CNH")
    else:

        if dif_dia <= 0:
            print("Sim, você já pode tirar sua CNH")
        else:
            print("Não, você ainda não pode tirar sua CNH")