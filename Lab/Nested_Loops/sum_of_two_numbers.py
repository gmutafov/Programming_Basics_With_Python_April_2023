start_number = int(input())
stop_number = int(input())
magic_number = int(input())

combination_is_found = False
counter_of_combinations = 0

for first_number in range(start_number, stop_number + 1):
    for second_number in range(start_number, stop_number + 1):
        counter_of_combinations += 1
        if first_number + second_number == magic_number:
            combination_is_found = True
            break
    if combination_is_found:
            break
if combination_is_found:
    print(f"Combination N:{counter_of_combinations} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{counter_of_combinations} combinations - neither equals {magic_number}")