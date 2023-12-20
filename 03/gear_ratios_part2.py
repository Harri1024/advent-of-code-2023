import re


def collect_number_coordinates(data):
    numbers_list = []
    pattern = r'(\d+)'
    for i, line in enumerate(data):
        numbers = re.finditer(pattern, line)
        if numbers:
            for number in numbers:
                numbers_list.append((i, number.span()[0], number.span()[1], int(number.group())))
    return numbers_list


def collect_symbol_coordinates(data):
    pattern = r'[^0-9\.]'
    symbols_list = []

    for i, line in enumerate(data):
        symbols = re.finditer(pattern, line.strip())
        if symbols:
            for symbol in symbols:
                symbols_list.append((i, symbol.span()[0], symbol.group()))
    return symbols_list

def check_adjacent_symbols(numbers_list, symbols_list):
    the_list = []
    the_dict = {}
    for number in numbers_list:
        for number_to_check in range(number[1] - 1, number[2] + 1):
            for offset in (-1, 0, 1):
                key = (number[0] + offset, number_to_check)
                for symbol in symbols_list:
                    x = (symbol[0], symbol[1])
                    if x == key:
                        #print(number)
                        the_list.append(number)
                        if symbol[2] == "*":
                            #print(symbol)
                            the_list.append(symbol)
                            if symbol not in the_dict:
                                the_dict[symbol] = []

                            the_dict[symbol] += [number]
                        break
    return the_dict




with open("03\data.txt") as f:
    data = f.readlines()

numbers_list = collect_number_coordinates(data)
#print(numbers_list)
symbols_list = collect_symbol_coordinates(data)
#print(symbols_list)
the_list = check_adjacent_symbols(numbers_list, symbols_list)
#print(the_list)
#print('---------------------------')

total_ratios = 0
for value in the_list.values():
    if len(value) == 2:
        print(value)
        total_ratios += value[0][3] * value[1][3]

print(total_ratios)


#print(build_duplicates_dict(the_list))
# part 1 total = 521515

#part2 total_ratios = 69527306