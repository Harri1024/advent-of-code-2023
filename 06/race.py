def read_data():
    with open("06\data.txt") as f:
        data = f.readlines()
        # data = f.read().replace("/n","")
        return data

print(read_data())


def calc(time, record_distance):
    sum = 0
    for i in range(time):
        factor = time - i
        distance = i * factor
        if distance > record_distance:
            sum += 1
    return(sum)

total = calc(61, 643) * calc(70, 1184) * calc(90, 1362) * calc(66, 1041)
print(total)
