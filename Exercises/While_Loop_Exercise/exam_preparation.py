command_for_end = 'Enough'
not_good_threshold = 4

total_grades = 0
count_grade = 0
last_problem_name = ''
count_not_good_grades = 0

not_good_grades_count_threshold = int(input())

while True:
    command = input()
    if command == command_for_end:
        break

    last_problem_name = command
    problem_grade = int(input())
    total_grades += problem_grade
    count_grade += 1

    if problem_grade <= not_good_threshold:
        count_not_good_grades += 1
        if count_not_good_grades >= not_good_grades_count_threshold:
            break
avg_grade = total_grades / count_grade
if command == command_for_end:
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {count_grade}")
    print(f"Last problem: {last_problem_name}")
else:
    print(f"You need a break, {count_not_good_grades} poor grades.")