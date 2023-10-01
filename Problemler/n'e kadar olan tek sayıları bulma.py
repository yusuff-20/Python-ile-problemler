# n'e kadar olan tek sayıları bulan program
n=int(input("Sayı Girin: "))
sayac = 0
while sayac < n:
    sayac += 1
    if sayac % 2 == 1:
        print(sayac,end=" ")