city = input()
sales = float(input())
commission = 0
# number = 100
# percents = number * 0.05
if city == 'Sofia':
    if 0 < sales <= 500: # if sales > 0 and sales <= 500
        commission = 0.05
    elif 500 < sales <= 1000:
        commission = 0.07
    elif 1000 < sales <= 10000:
        commission = 0.08
    elif sales > 10000:
        commission = 0.12
elif city == 'Varna':
    if 0 < sales <= 500:  # if sales > 0 and sales <= 500
        commission = 0.045
    elif 500 < sales <= 1000:
        commission = 0.075
    elif 1000 < sales <= 10000:
        commission = 0.1
    elif sales > 10000:
        commission = 0.13
elif city == 'Plovdiv':
    if 0 < sales <= 500:  # if sales > 0 and sales <= 500
        commission = 0.055
    elif 500 < sales <= 1000:
        commission = 0.08
    elif 1000 < sales <= 10000:
        commission = 0.12
    elif sales > 10000:
        commission = 0.145
if commission == 0:
    print('error')
else:
    income = sales * commission
    print(f'{income:.2f}')

