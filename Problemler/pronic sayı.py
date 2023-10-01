#pronic sayı
a = 0
n = int(input("bir sayı giriniz:"))
for i in range(1,n+1):
    if (n%i==0) and (n%(i+1)==0):
        a += 1
if a == 0:
    print("sayı pronic değildir.")
else:
    print("sayı pronictir.")