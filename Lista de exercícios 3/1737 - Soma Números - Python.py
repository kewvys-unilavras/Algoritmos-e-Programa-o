#https://www.beecrowd.com.br/judge/pt/custom-runs/code/396691

quant = int(input())
if quant > 0:
  cont=1
  soma =0
  while cont <= quant:
    num = float(input())
    soma = soma + num
    cont = cont +1
  print ("Soma dos números informados: ""%.2f" %soma)
else:
  print ("Informe uma quantidade > 0!")