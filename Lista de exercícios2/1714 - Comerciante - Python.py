#https://www.beecrowd.com.br/judge/pt/custom-runs/code/395278

valor_produto = float(input())
if valor_produto < 20:
 valor_venda = valor_produto * 1.45
else:
  valor_venda = valor_produto * 1.3

print("\nValor de venda: R$%.2f" %(valor_venda))
