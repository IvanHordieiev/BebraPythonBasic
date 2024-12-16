x = int(input("Intro un num menor 100: "))
y = 0.0
for i in range(x-4,1,-4):
    y += i**2
    print(i)
print("La suma dels quadrats de 4 en quatre de {} és {}".format(x, y))