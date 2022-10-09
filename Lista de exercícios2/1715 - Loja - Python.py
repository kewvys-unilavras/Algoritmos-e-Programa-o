#https://www.beecrowd.com.br/judge/pt/custom-runs/code/395372

id = int(input())
valor_compra = float(input())
if id == 1:
  desconto = valor_compra
  print("Valor total a ser pago: R$" "%.2f" % (desconto))
elif id == 2:
  desconto = valor_compra-(valor_compra * 0.13)
  print("Valor total a ser pago: R$" "%.2f" % (desconto))
elif id == 3:
   desconto = valor_compra-(valor_compra * 0.07)
   print("Valor total a ser pago: R$" "%.2f" % (desconto))
else:
  print("OPÇÃO INVÁLIDA!")
