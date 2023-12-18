import re

numbers_list = [(0, 12, 15), (0, 17, 20), (0, 27, 29), (2, 31, 34), (3, 31, 34)]
symbols_list = [(2, 15, '#'), (0, 16, '#'), (1, 34, '&'), (1, 38), '#', (4, 34, '#')]


for number in numbers_list:
    for number_to_check in range(number[1] - 1, number[2] + 1):
        for offset in (-1, 0, 1):
            if (number[0] + offset, number_to_check) in symbols_list:
                print(number)
                break 


list = [(1, 2), (4, 5)]
line = "1,2,3,4,5"

"""
if (4, 5) in list:
    print("joo")

pattern = r'(\d+)'
numbers = re.finditer(pattern, line)
for number in numbers:
    print(number)
"""