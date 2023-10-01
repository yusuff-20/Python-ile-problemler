# Girilen n değerine göre Fibonacci serisinin ( 0 1 2 3 5 8 … ) ilk n terimini hesaplayınız
n = int(input("bir sayı giriniz:"))
a = 0
b = 1
fib = 0
print(a,end=" ")
print(b,end=" ")
for i in range(n-2):
    fib = a+b
    a=b
    b=fib
    print(fib,end=" ")