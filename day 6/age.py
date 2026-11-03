while True:
    try:
        a = int(input("enter your age "))
        if a > 0 and a < 120:
            print(a)
            i = 0
            break
        else:
            print("rejected" )
    
    except ValueError:
        print("try again")            
     