budget = int(input())
season = input()
fishermen = int(input())

price = 0
discount = 0
extra_discount = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if fishermen <= 6:
    discount = 0.1
elif fishermen <= 11:
    discount = 0.15
else:
    discount = 0.25

if fishermen % 2 == 0 and season != 'Autumn':
    extra_discount = 0.05

total_price = price * (1 - discount) * (1 - extra_discount)

if budget >= total_price:
    print(f'Yes! You have {budget - total_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {total_price - budget:.2f} leva.')