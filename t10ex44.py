x = input("Intro num: ")
sum=0
for e in x:
    sum+=int(e)
if sum%2==0:
    print("La suma dels dígits del número {} és {} i és parell".format(x, sum))
else:
    print("La suma dels dígits del número {} és {} i és senar".format(x, sum))