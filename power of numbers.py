a = int(input("Saisir un entier positive"))
while a < 0:
    a = int(input("Saisir un entier positive"))
b = int(input("Saisir une base positive"))
while b < 0 or a < b:
    b = int(input("Saisir une base positive"))
y1 = b
i = 1
while (a != y1):
    y1 = b ** i
    i = i+1
    if a < y1:
         break

if a == y1 :
    print(b ,"**",i-1 ,"=",a)
else:
    print (b,"n'est pas une base de",a)