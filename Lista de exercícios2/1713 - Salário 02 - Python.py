#https://www.beecrowd.com.br/judge/pt/custom-runs/code/395191

valor_hora = float (input())
horas_trabalhadas = float(input())
salario_bruto = valor_hora*horas_trabalhadas
print("Salário bruto: R$" "%.2f" % salario_bruto) 

imposto = salario_bruto *0.11
print ("Imposto: R$""%.2f" %imposto)

inss= salario_bruto * 0.08
print("INSS: R$%.2f" % inss)

sindicato = salario_bruto * 0.05
print ("Sindicato: R$%.2f" % sindicato)

diferenca = imposto + inss + sindicato
salario_liquido = (salario_bruto - diferenca)
print ("Líquido: R$%.2f" % salario_liquido)