from math import ceil
series_name = input()
episode_time = int(input())
break_time = int(input())

lunch_time = break_time * 1/8
breather_time = break_time * 1/4
remaining_time = break_time - lunch_time - breather_time
diff = abs(remaining_time - episode_time)
rounded_diff = ceil(diff)
diff_2 = abs(episode_time - remaining_time)
rounded_diff_2 = ceil(diff_2)
if remaining_time >= episode_time:
    print(f'You have enough time to watch {series_name} and left with {rounded_diff} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need {rounded_diff_2} more minutes.")