import re

def first_and_last_digit(line):
    found_numbers = re.findall("\d", line)
    return int(found_numbers[0] + found_numbers[-1])

with open("1/input.txt") as file:
    lines = file.readlines()
    line_digits = map(first_and_last_digit, lines)
    print(sum(line_digits))
