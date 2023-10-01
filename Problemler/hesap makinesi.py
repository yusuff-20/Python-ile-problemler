# hesap makinesi
toplama = 1
cikarma = 2
carpma = 3
bolme = 4
karealma = 5

sayi1 = int(input("bir sayı giriniz:"))
sayi2 = int(input("bir sayı giriniz:"))
islem = int(input("işlem türü seçiniz:"))
if islem==1:
    print("bu işlemin sonucu", sayi1 + sayi2)
elif islem==2:
    print("bu işlemin sonucu", sayi1 - sayi2)
elif islem==3:
    print("bu işlemin sonucu", sayi1 * sayi2)    
elif islem==4:   
    print("bu işlemin sonucu", sayi1 / sayi2)
else:   
    print("bu işlemin sonucu", sayi1 ** sayi2)
