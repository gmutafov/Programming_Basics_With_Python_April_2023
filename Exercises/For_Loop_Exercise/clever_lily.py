age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

total_money = 0
# toy_count = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        total_money += birthday * 5
        total_money -= 1
    else:
        total_money += price_per_toy #toy_count += 1
if total_money >= washing_machine_price:
    print(f"Yes! {total_money - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - total_money:.2f}")