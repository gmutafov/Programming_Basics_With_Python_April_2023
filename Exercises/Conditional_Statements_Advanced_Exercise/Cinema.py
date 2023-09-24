premiere = 12.00
normal = 7.50
discount = 5.00
screening_type = input()
rows = int(input())
columns = int(input())

income = 0

cinema_capacity = rows * columns

if screening_type == "Premiere":
    income = cinema_capacity * premiere
elif screening_type == 'Normal':
    income = cinema_capacity * normal
elif screening_type == 'Discount':
    income = cinema_capacity * discount

print(f'{income:.2f} leva')
