a= int(input("enter the number of rows in a triangle"))
for i in range(1,a+1):
    for j in range(i):
        print ("*", end="")
        a= a -1

    print()