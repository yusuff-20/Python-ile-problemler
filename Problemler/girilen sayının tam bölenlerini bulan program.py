# Girilen sayının tam bölenlerini bulan program
sayi=int(input("Sayıyı Girin: "))
print("tam bölenleri:")
for i in range(1,sayi+1):
    if (sayi % i == 0):
        print(i,end=" ")