#harshad sayı
sayi = input("sayı giriniz:")
x = 0
toplam = 0
for rakam in sayi:
    toplam += int(rakam)
    
print("sayının rakamları toplamı:",toplam)
a = int(sayi)
for i in range(a):
    if int(sayi) % toplam == 0:
        x += 1

if x == 0:
    print("harshad değil")
else:
     print("harshad ")