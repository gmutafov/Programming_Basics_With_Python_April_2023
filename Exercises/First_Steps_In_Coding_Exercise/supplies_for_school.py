PENS_PRICE = 5.80
MARKERS_PRICE = 7.20
DETERGANT_PRICE = 1.20

pens_count = int(input())
markers_count = int(input())
detergant_leters = int(input())
discount_percent = int(input())

total_sum = pens_count * PENS_PRICE \
            + markers_count * MARKERS_PRICE \
            + DETERGANT_PRICE * detergant_leters
total_sum_with_discount = total_sum * (100 - discount_percent) / 100
print(total_sum_with_discount)
