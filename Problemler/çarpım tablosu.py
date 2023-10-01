# çarpım tablosu
x = int(input("Lütfen tablo boyutunu giriniz:"))
a = 0

for i in range (1,x+1):
    print(i, end="  ")

print( "\n +", "-"*(x+x+x), end=" ")

for i in range (1,x+1):
    print("\n", i , "|" , end=" ")
    a += 1
    for i in range (1,x+1):
        print((i)*a , end= " ")