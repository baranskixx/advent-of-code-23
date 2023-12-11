def read_input(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines() if line != '\n']

if __name__ == '__main__':
    lines = read_input('input.txt')
    galaxies = []
    rows = [False] * len(lines)
    columns = [False] * len(lines[0])

    for y, line in enumerate(lines):
        for x, point in enumerate(line):
            if point == '#':
                galaxies.append((y, x))
                rows[y] = True
                columns[x] = True
    
    sum = 0
    for a in range(len(galaxies)):
        for b in range(a+1, len(galaxies)):
            sum += abs(galaxies[a][0] - galaxies[b][0]) + abs(galaxies[a][1] - galaxies[b][1])
            row_range_low = min(galaxies[a][0], galaxies[b][0])
            row_range_high = max(galaxies[a][0], galaxies[b][0])
            for y in range(row_range_low+1, row_range_high):
                if not rows[y]:
                    sum += 999999
            col_range_low = min(galaxies[a][1], galaxies[b][1])
            col_range_high = max(galaxies[a][1], galaxies[b][1])
            for x in range(col_range_low+1, col_range_high):
                if not columns[x]:
                    sum += 999999

    print(sum)