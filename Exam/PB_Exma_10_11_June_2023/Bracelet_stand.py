pocket_money = float(input())
income_per_day = float(input())
expenses = float(input())
present_price = float(input())

total_pocket_money = pocket_money * 5
income = income_per_day * 5
total_income = (total_pocket_money + income) - expenses

if total_income >= present_price:
    print(f"Profit: {total_income:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {present_price - total_income:.2f} BGN.")