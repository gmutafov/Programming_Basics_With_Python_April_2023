annual_fee = int(input())

basketball_shoes = annual_fee * 0.6
basketball_team = basketball_shoes * 0.8
basketball = basketball_team * 0.25
basketball_accessories = basketball * 0.2

total_cost = annual_fee + basketball_team + basketball + basketball_accessories + basketball_shoes

print(f"Jesse's total expenses for playing basketball would be: {total_cost} lv.")