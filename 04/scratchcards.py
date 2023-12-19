import re


with open("04\data.txt") as f:
    data = f.readlines()


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

answer = 0
for x in calculate_hits_on_rows(data):
    answer += calculate_pattern(x)

print(answer)

