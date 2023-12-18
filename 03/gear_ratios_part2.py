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
    total = 0
    for number in numbers_list:
        for number_to_check in range(number[1] - 1, number[2] + 1):
            for offset in (-1, 0, 1):
                
                for symbol in symbols_list:
                    if (number[0] + offset, number_to_check) is (symbol[0], symbol[1]):
                        print("symbol[2]")
                         
                    #print(number)
                    #total += number[3]
                    #break 
    return total


with open("03\data.txt") as f:
    data = f.readlines()

numbers_list = collect_number_coordinates(data)
#print(numbers_list)
symbols_list = collect_symbol_coordinates(data)
#print(symbols_list)
total = check_adjacent_symbols(numbers_list, symbols_list)
print(total)

# total = 521515