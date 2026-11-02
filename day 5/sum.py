a = int(input("enter a number"))
i = a
b = 0 
while i != 0:
    r = i % 10
    q = a // 10
    b = b + r
    i= i // 10


print(f"the total sum is {b}")
