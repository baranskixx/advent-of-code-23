def read_input(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines() if line != '\n']
    
if __name__ == '__main__':
    lines = read_input('sample.txt')
    _sum = 0
    for line in lines:
        values = [int(number) for number in line.split()]
        interpolations = [values]
        while True:
            next_inter = []
            for i in range(len(interpolations[-1]) - 1):
                x = interpolations[-1][i]
                y = interpolations[-1][i+1]
                next_inter.append(y - x)
            interpolations.append(next_inter)
            if next_inter.count(0) == len(next_inter):
                break
        added_value = 0
        for i in range(len(interpolations)-2, -1, -1):
            added_value = interpolations[i][0] - added_value
        _sum += added_value
    
    print(_sum)
