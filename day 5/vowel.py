a = str(input(" enter a sentence = "))
d = 0
c= len(a)
for i in range(c):
    b = a[i]
    if b == "a" or b == "e" or b == "i" or b == "o" or b == "u":
        d = d + 1

print(f"the number of vowel letter is {d}")