# Girilen n ve k değerlerine göre k + 2k + 3k + ...+nk yı hesaplayan program
n = int(input("n:"))
k = int(input("k:"))
a = 0
for i in range(1,n+1):
    a += k*i
print(a)
