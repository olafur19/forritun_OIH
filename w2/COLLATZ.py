a0 = int(input("Input a positive int: "))   # Do not change this line
while a0 != 1:
    print(a0)
    if a0 % 2 == 0:
        a0 = a0 // 2
    else:
        a0 = ((a0*3) + 1)
print(1)
        