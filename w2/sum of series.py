length = int(input("Input the length of series: "))
num = 0
total = 0
for i in range(1, length+1):
    num = i * 2
    if num % 4 == 0:
        num *= -1
    else:
        print(num)
        total += num
        continue
    print(num)
    total += num

print("Sum:", total)