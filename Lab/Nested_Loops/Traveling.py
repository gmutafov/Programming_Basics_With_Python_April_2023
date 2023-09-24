destination = input()


while destination != 'End':
    money_needed = float(input())
    current_money = 0
    while current_money < money_needed:
        saved_money = float(input())
        current_money += saved_money
    print(f"Going to {destination}!")
    destination = input()
    