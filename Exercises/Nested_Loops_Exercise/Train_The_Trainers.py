judges = int(input())
command = input()
total_presentation_sum = 0
presentation_count = 0

while not command == 'Finish':
    current_presentation = command
    current_presentation_sum = 0

    for _ in range(judges):
        current_judge_score = float(input())
        current_presentation_sum += current_judge_score
        # total_presentation_sum += current_judge_score
    total_presentation_sum += current_presentation_sum
    presentation_count += 1
    avg_score = current_presentation_sum / judges
    print(f"{current_presentation} - {avg_score:.2f}.")

    command = input()
avg_total_score = total_presentation_sum / (presentation_count * judges)
print(f"Student's final assessment is {avg_total_score:.2f}.")