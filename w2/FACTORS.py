n = int(input("Input an int: ")) # Do not change this line
div_num = 1

while div_num <= n:
    if n % div_num == 0:
        print(div_num)
        div_num += 1
    else:
        div_num += 1

