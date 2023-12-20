data = [('20', 'green'), ('3', 'red'), ('2', 'blue'), ('9', 'red'), ('16', 'blue'), ('18', 'green'), ('6', 'blue'), ('19', 'red'), ('10', 'green'), ('12', 'red'), ('19', 'green'), ('11', 'blue')]

def multibly_max_colors(row_data)
    game = {'green': 0,
        'blue': 0,
        'red': 0}

    sorted = sorted(data)
    print(sorted)

    sorted = data.sort(key=lambda x: x[0], reverse=True)
    print("-------")
    print(data)

    max_num = 0
    for num, color in data:
        if int(game[color]) < int(num):
            game[color] = num
        print(game)

    total = int(game['blue']) * int(game['green']) * int(game['red'])
    print(total)
    return total