DOG_PRICE = 2.50
CAT_PRICE = 4.00
dogs_food = int(input())
cats_food = int(input())

total_price = dogs_food * DOG_PRICE + \
    cats_food * CAT_PRICE
print(f"{total_price} lv.")


