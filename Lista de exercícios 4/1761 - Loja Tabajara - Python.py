#https://www.beecrowd.com.br/judge/pt/custom-runs/code/404010

compra = float(input())
soma = compra
while compra > 0:
    compra = float(input())
    soma = soma + compra
        
valorPago = float(input())
troco = valorPago-soma   
print ("Total da compra: R$%.2f" %soma)
print ("Valor pago: R$%.2f" %valorPago)
print ("Troco: R$%.2f" %troco)