import re


number_mapping = {
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

with open("data.txt") as f:
    data = f.readlines()


converted = []
for line in data:
    for word, number in number_mapping.items():
        line = re.sub(word, number, line)

    converted.append(line)
    print(line)

print(converted)

total = 0
for line in converted:
    x = re.findall('[0-9]{1}', line)
    num = (x[0] + x[-1])
    print("----------")
    print(num)
    print(line)

    print(num)
    total += int(num)

print(total)
