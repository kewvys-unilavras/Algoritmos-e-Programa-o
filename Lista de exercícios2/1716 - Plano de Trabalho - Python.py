#https://www.beecrowd.com.br/judge/pt/custom-runs/code/395348

id = input()
salario_inicial = float(input())

if id == 'A':
   aumento=salario_inicial*1.10
elif id == 'B':
       aumento=salario_inicial*1.15
elif id == 'C':
       aumento=salario_inicial*1.20

print("Novo salário: R$%.2f" %aumento)
