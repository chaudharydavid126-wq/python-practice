a= input("in what form do you want to input in number or alphabet")
i = 1
if a == "n" or a == "number":
    while i != 0:
        try:
            for i in range(4):
                b = int(input()) 
                i = 0

        except ValueError:
            print("try again")
            i = i + 1

else:
    j = int(input("for alphabet how long will you make "))
    while j != 0:
            b=str(input("enter the alphabet"))
            j =  j - 1
        