start_height = 5364
target = 8848
current_height = 0
count = 1
while True:
    yes_or_no = input()
    if yes_or_no == "END":
        break
    if yes_or_no == "Yes":
        count += 1
    if count > 5:
        break
    height = int(input())
    current_height += height
    if current_height + start_height >= target:
        break
if start_height + current_height < target:
    print("Failed!")
    print(f"{start_height + current_height}")
else:
    print(f"Goal reached for {count} days!")