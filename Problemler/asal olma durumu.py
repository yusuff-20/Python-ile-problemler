# Bir sayının asal olup olmadığını bulan program
n = int(input("bir sayı giriniz:"))
c = 0
if n == 1:
    c += 1
for i in range(2,n):
    if (n%i == 0):
        c += 1
        break
if c==0:
    print("sayı asaldır")
else:
    print("sayı asal değildir")
