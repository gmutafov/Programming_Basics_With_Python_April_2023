number1 = int(input())
number2 = int(input())

for num in range(number1, number2 + 1):
    number_to_str = str(num)
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if even_sum == odd_sum:
        print(num, end=' ')
