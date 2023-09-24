ROSE = 5
DAHLIA = 3.80
TULIPS = 2.80
NARCISSUS = 3
GLADIOLUS = 2.50

price = 0
discount = 0

flower_type = input()
flower_count = int(input())
budget = int(input())

if flower_type == 'Roses':
    price = ROSE
    if flower_count > 80:
        discount = 0.1
elif flower_type == 'Dahlias':
    price = DAHLIA
    if flower_count > 90:
        discount = 0.15
elif flower_type == 'Tulips':
    price = TULIPS
    if flower_count > 80:
        discount = 0.15
elif flower_type == 'Narcissus':
    price = NARCISSUS
    if flower_count < 120:
        discount = -0.15
elif flower_type == 'Gladiolus':
    price = GLADIOLUS
    if flower_count < 80:
        discount = -0.20

total_price = flower_count * price * (1 - discount)

if budget >= total_price:
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and '
          f'{budget - total_price:.2f} leva left.')
else:
    print(f'Not enough money, you need {total_price - budget:.2f} leva more.')