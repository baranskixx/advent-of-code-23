def load_input(path):
    with open('input.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_number_end(line, num_start):
    num_end = num_start + 1
    while num_end < len(line) and line[num_end].isdigit():
        num_end += 1
    
    return num_end

if __name__ == '__main__':
    lines = load_input('input.txt')
    _sum = 0
    for y, line in enumerate(lines):
        x = 0
        while x < len(line):
            if line[x].isdigit():
                _end = find_number_end(line, x)
                adjacent_same_row = (x > 0 and line[x-1] != '.') or (_end < len(line) and line[_end] != '.')
                a, b = max(x-1, 0), min(_end+1, len(line))
                adjacent_upper_row = y-1 > 0 and True in \
                [(not lines[y-1][i].isdigit()) and (lines[y-1][i] != '.') for i in range(a, b)]
                adjacent_lower_row = y+1 < len(lines) and True in \
                [(not lines[y+1][i].isdigit()) and (lines[y+1][i] != '.') for i in range(a, b)]
                if adjacent_lower_row or adjacent_upper_row or adjacent_same_row:
                    _sum += int(line[x : _end])
                x = _end
            else:
                x += 1
    print(_sum)
