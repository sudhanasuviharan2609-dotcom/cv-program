age =int(input("enter your age:"))
if age>=18:
    weg=int(input("enter the weight:"))
    if weg>50:
        print("can donate blood")
    else:
        print("under weight")

else:
    print("under age")    