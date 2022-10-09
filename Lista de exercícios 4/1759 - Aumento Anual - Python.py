#https://www.beecrowd.com.br/judge/pt/custom-runs/code/404011

ano = int(input())
salario= 1000.00
taxa = 0.015
if ano < 2006:
    print("O ano informado deverá ser > 2005!")
else:
    aumento=salario+(salario*taxa)
    while(2007<=ano):
        taxa= taxa + 0.01
        aumento=aumento+(aumento*taxa)
        ano = ano -1
    print("Salário atual: R$%.2f"%aumento)