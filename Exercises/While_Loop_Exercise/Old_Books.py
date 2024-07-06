target_book = input()
book_count = 0
command = input()
while command != target_book:
    book = command
    if command == 'No More Books':
        break
    book_count += 1
    command = input()
if command == 'No More Books':
    print(f"The book you search is not here!\nYou checked {book_count} books.")
else:
    print(f"You checked {book_count} books and found it.")