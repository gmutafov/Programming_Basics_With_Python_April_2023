age = float(input())
gender = input()

if gender == "m":
    if age >= 16:
        print('Mr.')
    else: # elif age < 16
        print('Master')

elif gender == 'f': #else
    if age >= 16:
        print('Ms.')
    else: # elif age < 16
        print('Miss')