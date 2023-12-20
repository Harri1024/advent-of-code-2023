import re


with open("04\data.txt") as f:
    data = f.readlines()
"""
data = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']
"""


def calculate_pattern(n):
    x = 1
    for y in range(n - 1):
        x = x * 2
    if n == 0:
        x = 0
    return x

def calculate_hits_on_rows(data):
    all_sums = []
    for line in data:
        x = re.split(r'[:|]', line)
        sum = 0
        pattern = r'(\d+)'
        for num in re.findall(pattern, x[2]):
            if num in re.findall(pattern, x[1]):
                sum += 1

        all_sums.append(sum)
    return all_sums


all_sums =  calculate_hits_on_rows(data)
cards = [1] * len(all_sums)

for x, stack in enumerate(cards):
    for i in range(stack):
        for y in range(all_sums[x]):
            cards[x+y+1] += 1

answer = 0
for x in all_sums:
    answer += calculate_pattern(x)
print(f"part 1 : {answer}")
print(f"part 2 : {sum(cards)}")

