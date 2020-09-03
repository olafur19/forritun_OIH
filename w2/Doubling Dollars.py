max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))
count = 1
days_when_amount_acquired = 0
for i in range(0, max_days+1):
    if count <= target:
        count = count*2
        days_when_amount_acquired += 1

if days_when_amount_acquired > max_days:
    days_when_amount_acquired = 0



print('Days needed:',days_when_amount_acquired)