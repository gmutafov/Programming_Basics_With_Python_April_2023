vacation_cost = float(input())
budget = float(input())
days_counter = 0
spend_counter = 0

while budget < vacation_cost and spend_counter < 5:
    command = input()
    money = float(input())
    days_counter += 1
    if command == 'save':
        budget += money
        spend_counter = 0
    elif command == 'spend':
        budget -= money
        spend_counter += 1
        if budget < 0:
            budget = 0

if spend_counter == 5:
    print(f"You can't save the money.")
    print(f"{days_counter}")
else:
    print(f"You saved the money for {days_counter} days.")
