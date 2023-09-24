PUZZLE_PRICE = 2.60
TALKING_DOLL = 3.00
PLUSHY_BEAR = 4.10
MINION = 8.20
TRUCK = 2.00

trip_price = float(input())
puzzle_numbers = int(input())
talking_doll_numbers = int(input())
plushy_bears_numbers = int(input())
minion_numbers = int(input())
truck_numbers = int(input())

total_toys = puzzle_numbers + talking_doll_numbers + plushy_bears_numbers + minion_numbers + truck_numbers

discount = 0

if total_toys >= 50:
    discount = 0.25
total_income = puzzle_numbers * PUZZLE_PRICE + talking_doll_numbers * TALKING_DOLL \
    + plushy_bears_numbers * PLUSHY_BEAR + minion_numbers * MINION \
    + truck_numbers * TRUCK

total_income_with_discount = total_income * (1 - discount)
rent_cost = total_income_with_discount * 0.10

final_income = total_income_with_discount - rent_cost

if final_income >= trip_price:
    print(f"Yes! {final_income - trip_price :.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - final_income :.2f} lv needed.")
