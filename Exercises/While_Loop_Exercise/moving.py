width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())

total_free_space = width_free_space * height_free_space * length_free_space
left_space = total_free_space

command = input()

while command != "Done":
    current_box = int(command)
    left_space -= current_box
    if left_space <= 0:
        break



    command = input()

if command == 'Done':
    print(f"{left_space} Cubic meters left.")
else:
    print(f"No more free space! You need {-left_space} Cubic meters more.")