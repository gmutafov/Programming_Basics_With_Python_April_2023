num = int(input())
if num <= 100:
    bonus = 5
elif num > 100:
    bonus = 0.20 * num
else:
    bonus = 0.10 * num

if num % 2 == 0:
    bonus = bonus + 1
elif num % 10 == 5:
    bonus = bonus + 2

print(bonus)
print(bonus + num)