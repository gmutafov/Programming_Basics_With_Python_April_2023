n = int(input())
n_str = str(n)

for x1 in range(1, int(n_str[2]) + 1):
    for x2 in range(1, int(n_str[1]) + 1):
        for x3 in range(1, int(n_str[0]) + 1):
            result = x1 * x2 * x3
            print(f'{x1} * {x2} * {x3} = {result};')