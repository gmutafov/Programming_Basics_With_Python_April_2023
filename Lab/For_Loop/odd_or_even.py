n = int(input())
sum_even = 0
sum_odd = 0
sum_total = 0
for i in range(0, n):
    if i % 2 == 0:
        sum_even = sum_even + int(input())
    else:
        sum_odd = sum_odd + int(input())

if sum_even == sum_odd:
    print("Yes")
    print(f"Sum = {sum_even}")
else:
    diff = abs(sum_even - sum_odd)
    print("No")
    print(f"Diff = {diff}")