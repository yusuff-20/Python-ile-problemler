# Girilen 3 basamaklı sayının basamak değerleri çarpımını bulunuz
n=int(input("3 basamaklı sayı Girin: "))
sayac = 0
while (sayac < n+1):
    sayac += 1
    if (100 <= n <= 999):
        print("Sayı geçerli")
        yb = (n//100)*100
        bb = (n % 10)
        ob = (n-yb) - bb
        islem =(yb) * (bb) * (ob)
        print(f"Bu sayının basamaklar değerleri çarpımı: {islem}")
        break
    else:
        print("Geçerli değer aralığında bir sayı giriniz.")
        break

