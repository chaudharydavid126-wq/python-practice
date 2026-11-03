i = 1
while i != 0:
    try:
        a = int(input("enter the interger"))
        print (a)
        i = 0
    except ValueError:
        print("it is not a interger try again")
        i = i + 1
