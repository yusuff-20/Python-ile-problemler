# n’e kadar ki tek sayıların toplamı, çift sayıların çarpımını hesaplayan program
n = int(input("bir sayı giriniz:"))
toplam = 0
carpim = 1
for i in range(1,n+1,1):
    if (i%2 == 1):
        toplam += i
        print("tek sayıların toplamı:",toplam, end = "  ")
    else:
        carpim *= i
        print("çift sayıların çarpımı:",carpim)