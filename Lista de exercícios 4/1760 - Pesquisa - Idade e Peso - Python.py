#https://www.beecrowd.com.br/judge/pt/custom-runs/code/403514

contPeso = 0
totalIdade= 0
for x in range(4):
    idade = int(input())
    peso = float(input())
    totalIdade = totalIdade + idade
    if peso > 90:
        contPeso = contPeso +1
    else:
        contPeso = contPeso+0

media = totalIdade/4
print("Qtd pessoas > 90 Kg: %i" %(contPeso))
print("Idade média: %.2f" %media)