# a üssü b yi açık hesaplayan program?
a = int(input("a'ya bir değer atayınız:"))
b = int(input("b'ye bir değer atayınız:"))
carpim = 1
for i in range(b):
    carpim *= a
print("a üssü b :",carpim)