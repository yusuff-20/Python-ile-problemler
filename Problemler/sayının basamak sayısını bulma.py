# Girilen bir sayının basamak sayısını veren program (sonsuza kadar)
n = int(input("bir sayı giriniz:"))
a = 1
basamak_sayisi = 0
while True:
    if (n / a > 0):
        basamak_sayisi += 1
        a *= 10
        continue
    else: 
        break
print("Basamak sayısı",basamak_sayisi)