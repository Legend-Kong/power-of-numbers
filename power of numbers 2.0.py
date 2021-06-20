a = int(input("Saisir un entier a: "))
a1 = a
j=0
for i in range(2,a):
   if a1 % i == 0:
        while (a % i == 0):
            a = a/i
            j = j + 1
        if a == 1:
            print (i,"**",j ,"=",a1)

        a = a1
        j=0



