n = int(input("Input an int: ")) # Do not change this line
div_num = 1
factor = 0

while div_num <= n/2:
    if n % div_num == 0:
        factor = n / div_num
        print(factor)
        div_num += 1

    

# Fill in the missing code below