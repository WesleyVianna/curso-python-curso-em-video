'''
Desafio 039
Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date


atual = date.today().year
nasc = int(input("Digite o seu Ano de Nascimento: "))
idade = atual - nasc

print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))

if idade == 18:
    print("Você tem que se alistar IMEDITAMENTE!")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos para o alistamento.".format(saldo))
    ano = atual + saldo
    print("Seu alistamento será em {}.".format(ano))
else:
    saldo = idade - 18
    print("Você já deveria ter se apresentado há {} anos.".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}.".format(ano))