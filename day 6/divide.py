a = int(input("enter a number in numinator"))

while True:
    try:
        b = int(input("enter the number for denominator"))
        c= a/b
        print(c)
        break

    except ZeroDivisionError:
        print("its zero so try again")

    except ValueError:
        print(input("its not a number try again"))


