models = int(input())

saler_1 = 0
saler_2 = 0
saler_3 = 0
saler_4 = 0
saler_5 = 0
saler_6 = 0
saler_7 = 0
saler_8 = 0
saler_9 = 0
saler_10 = 0
avg_rating = 0

for i in range(1, models + 1):
    computer_count = int(input())

    rating = 0
    avg_sales = 0
    sales_placed = 0

    if computer_count % 10 == 2:
        avg_rating += 2
        rating = 0
        avg_sales = computer_count // 10
        sales_placed = avg_sales * rating
    elif computer_count % 10 == 3:
        avg_rating += 3
        rating = 0.5
        avg_sales = computer_count // 10
        sales_placed = avg_sales * rating
    elif computer_count % 10 == 4:
        avg_rating += 4
        rating = 0.70
        avg_sales = computer_count // 10
        sales_placed = avg_sales * rating
    elif computer_count % 10 == 5:
        avg_rating += 5
        rating = 0.85
        avg_sales = computer_count // 10
        sales_placed = avg_sales * rating
    elif computer_count % 10 == 6:
        avg_rating += 6
        rating = 1
        avg_sales = computer_count // 10
        sales_placed = avg_sales * rating

    if i == 1:
        saler_1 += sales_placed
    elif i == 2:
        saler_2 += sales_placed
    elif i == 3:
        saler_3 += sales_placed
    elif i == 4:
        saler_4 += sales_placed
    elif i == 5:
        saler_5 += sales_placed
    elif i == 6:
        saler_6 += sales_placed
    elif i == 7:
        saler_7 += sales_placed
    elif i == 8:
        saler_8 += sales_placed
    elif i == 9:
        saler_9 += sales_placed
    elif i == 10:
        saler_10 += sales_placed

total_sales = saler_1 + saler_2 + saler_3 + saler_4 + saler_5 + saler_6 + saler_7 + saler_8 \
    + saler_9 + saler_10

total_avg_rating = avg_rating / models
print(f"{total_sales:.2f}")
print(f"{total_avg_rating:.2f}")

