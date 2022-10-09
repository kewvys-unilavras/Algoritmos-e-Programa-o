#https://www.beecrowd.com.br/judge/pt/custom-runs/code/396677

num=int(input())
fat = 1
aux = 1
while aux <= num:
 fat *= aux
 aux = aux +1
print ("%i" "! = " "%i" % (num,fat))
