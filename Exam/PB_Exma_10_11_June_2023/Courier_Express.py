weight = float(input())
kind_of_service = str(input())
distance = int(input())

price_for_km = 0
expenditure = 0

if weight < 1:
    price_for_km = 3
elif 1 <= weight < 10:
    price_for_km = 5
elif 10 <= weight < 40:
    price_for_km = 10
elif 40 <= weight < 90:
    price_for_km = 15
elif 90 <= weight:
    price_for_km = 20

if kind_of_service == 'express':
    if weight < 1:
        expenditure = 3 * 0.8 * weight
    elif 1 <= weight < 10:
        expenditure = 5 * 0.4 * weight
    elif 10 <= weight < 40:
        expenditure = 10 * 0.05 * weight
    elif 40 <= weight < 90:
        expenditure = 15 * 0.02 * weight
    elif 90 <= weight:
        expenditure = 20 * 0.01 * weight

total_price = (price_for_km + expenditure) * distance / 100

print(f'The delivery of your shipment with weight of {weight:.3f} kg. would cost \
{total_price:.2f} lv.')
