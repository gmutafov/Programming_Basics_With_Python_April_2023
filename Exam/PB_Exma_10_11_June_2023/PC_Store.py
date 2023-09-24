usd_cpu = float(input())
usd_gpu = float(input())
usd_ram = float(input())
ram_count = int(input())
discount = float(input())

cpu_bgn = usd_cpu * 1.57
gpu_bgn = usd_gpu * 1.57
ram_bgn = usd_ram * 1.57
ram = ram_bgn * ram_count
cpu_discount = cpu_bgn - (cpu_bgn * discount)
gpu_discount = gpu_bgn - (gpu_bgn * discount)
total_price = cpu_discount + gpu_discount + ram

print(f"Money needed - {total_price:.2f} leva.")