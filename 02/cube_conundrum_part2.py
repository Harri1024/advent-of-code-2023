import re


def compare_tuples_with_dict(game_tuple, rule):
    for value, color in game_tuple:
        if int(value) > rule.get(color, 0):
            return False
    return True

def multibly_max_colors(row_data):
    game = {'green': 0,
        'blue': 0,
        'red': 0}

    for num, color in row_data:
        if int(game[color]) < int(num):
            game[color] = num
        #print(game)

    total = int(game['blue']) * int(game['green']) * int(game['red'])
    #print(total)
    return total

with open("02\data.txt") as f:
    data = f.readlines()
    
# only 12 red cubes, 13 green cubes, and 14 blue cubes
rule= {'red': 12,
       'green': 13,
       'blue': 14}
total = 0
max_colors_total = 0
pattern = r'(\d+) (blue|red|green)'
for line in data:
    #print("-----------")
    game = {'green': 0,
       'blue': 0,
       'red': 0}
    #print(line)
    color_digit = re.findall(pattern, line)
    max_colors_total += multibly_max_colors(color_digit)
    #print(digits)

    #for digit, color in digits:
    #    game[color] += int(digit)
    #print(color_digit)
    
    if (compare_tuples_with_dict(color_digit, rule)):
        split = line.split(':') 
        s = ''.join(x for x in split[0] if x.isdigit())
        #print(color_digit)
        #print(s)
        total += int(s)
print(total)
print(max_colors_total)