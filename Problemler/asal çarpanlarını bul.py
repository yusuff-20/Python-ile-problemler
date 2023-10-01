# Girilen bir sayının asal çarpanlarını bulan program
n = int(input("bir sayı giriniz:"))
a = 2
b = 0
while n > 1:
    if (n%a > 0):
        a += 1
    else:
        n /= a
        b += 1
        if b == 1:
            print(a)