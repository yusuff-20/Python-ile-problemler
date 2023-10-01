# Klavyeden girilen 3 basamaklı sayının basamak değerlerini yazdıran program

a = int(input("3 basamaklı bir sayı giriniz:"))
yb = (a//100)*100
bb = a%10
ob = (a%100)-bb
print(f"birler basamağı:{bb}")
print(f"onlar basamağı:{ob}")
print(f"yüzler basamağı:{yb}")