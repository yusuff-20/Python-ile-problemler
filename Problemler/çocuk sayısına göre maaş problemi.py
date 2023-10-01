# İşçi maaşı , çocuk sayısı verilmiştir. Çocuk sayısı bir ise %5, iki ise %10, üç veya daha ise fazla %15 zam yapan program
maas = int(input("Maaş giriniz:"))
cocukSayisi = int(input("Çocuk sayısı giriniz:"))
if (cocukSayisi == 0):
    print(f"Maaşınız:{maas}")
elif (cocukSayisi == 1):
    islem = (maas) + (maas*5)/100
    print(f"Maaşınız:{islem}")
elif (cocukSayisi == 2):
    islem2 = (maas) + (maas*10)/100
    print(f"Maaşınız:{islem2}")
else:
    islem3 = (maas) + (maas*15)/100
    print(f"Maaşınız:{islem3}")