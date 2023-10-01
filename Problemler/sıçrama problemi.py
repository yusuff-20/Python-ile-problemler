# örnek52 X m'den bırak Her sıçramada %20 yükseklik kaybet 1 metreden az olana kadar aldığı yolu ve sıçrama sayısını bul
x = int(input("yükseklik giriniz:"))
a = 0
sıcr = 0
topyol = 0
while a < 1:
    x -= (x*20)/100
    if x > 1:
        topyol += x + (x*80)/100
        sıcr += 1 
        continue
    else:
        a += 1
print("alınan toplam yol:",topyol)
print("sıçrama sayısı:",sıcr)
