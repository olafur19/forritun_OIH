#Algorithm that prints n length of the following sequence
#the following number of the sequence is a sum of the previous 3 numbers


n = int(input("Enter the length of the sequence: ")) # Do not change this line
num_1 = 0
num_2 = 0
num_3 = 1
num_sum = 0

for i in range(1, n+1):
    num_1 = num_2
    num_2 = num_3
    num_3 = num_sum
    num_sum = num_1 + num_2 + num_3
    print(num_sum)