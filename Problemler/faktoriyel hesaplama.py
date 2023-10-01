# Girilen sayının faktöriyelini hesaplayan program
a = int(input("a'ya bir değer atayınız:"))
carpim = 1
for i in range(1,a+1):
    carpim *= i
print("Girilen sayının faktöriyeli:",carpim)