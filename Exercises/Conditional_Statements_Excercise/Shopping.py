budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

total_gpu = gpu_count * 250
total_cpu = 0.35 * total_gpu * cpu_count
total_ram = 0.10 * total_gpu * ram_count

total_price = total_gpu + total_cpu + total_ram

if gpu_count > cpu_count:
    total_price = total_price * 0.85

if budget >= total_price:
    print(f'You have {budget - total_price :.2f} leva left!')
else:
    print(f'Not enough money! You need {total_price - budget :.2f} leva more!')