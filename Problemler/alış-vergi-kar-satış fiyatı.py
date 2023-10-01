# Bir ürünün alış fiyatı, vergi ve kar oranlarını kullanılarak satış fiyatını hesaplayan program
a = int(input("alış fiyatı giriniz:"))
b = int(input("vergi oranı giriniz:"))
c = int(input("kar oranı giriniz:"))
satisFiyati = a + (a/100)*b + (a/100)*c
print(satisFiyati)