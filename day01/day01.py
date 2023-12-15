import re


def replace_digit_word(digit_word):
    digit_word_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    if digit_word in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        return int(digit_word)
    else:
        return digit_word_dict[digit_word]


with open('input1') as input_file:
    digit_sum = 0
    for line in input_file:
        search_result = re.findall(r'([0-9])', line)
        digit_sum += (int(search_result[0]) * 10 + int(search_result[-1]))
    print('result1:', digit_sum)

with open('input2') as input_file:
    digit_sum = 0
    for line in input_file:
        search_result = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|zero|[0-9]))', line)
        first_digit = replace_digit_word(search_result[0])
        last_digit = replace_digit_word(search_result[-1])
        digit_sum += (first_digit * 10 + last_digit)
    print('result2:', digit_sum)
