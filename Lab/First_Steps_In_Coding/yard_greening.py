PER_SQUARE_METER = 7.61
DISCOUNT = 0.18

square_meters_to_be_done = float(input())
total_meters_price = square_meters_to_be_done * PER_SQUARE_METER

discount_price = total_meters_price * DISCOUNT
total_price = total_meters_price - discount_price
print(f"The final price is {total_price} lv.")
print(f"The discount is {discount_price} lv.")