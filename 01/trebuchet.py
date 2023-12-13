import re


def numbers_to_int(s):

    numbers = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'  

    converted = ""
    s = s.replace("\n", "")
    digits = re.findall(regex, s)
    #print(digits)
    for digit in digits:
        converted += str(numbers.get(digit, digit))

    #print(converted)

    return converted


with open("01\data.txt") as f:
    data = f.readlines()
count = 0
total = 0
for line in data:
    line_new = numbers_to_int(line)
    x = re.findall('[0-9]{1}', line_new)
    line_number = (x[0] + x[-1])
    #print("----------")
    #print(x)
    #print(line[:-1])
    #print(line_new[:-1])
    print(line_number)

    total += int(line_number)
    count += 1
print("**********")
print(total)
