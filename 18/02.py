
INF = 1e12
DIR_TO_MOVE = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]


def read_input(path):
    with open(path, 'r') as file:
        return [line.strip().split() for line in file.readlines()]    

 
def shoelace_area(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    return abs(sum([x[i] * (y[(i + 1) % len(y)] - y[i - 1]) for i in range(len(x))])) // 2

def calculate_area(moves):
    points = [(0, 0)]
    for dir, _, color in moves:
        l = int(color[2:7], 16)
        move_index = int(color[7])
        move_y, move_x = DIR_TO_MOVE[move_index - 1]
        y, x = points[-1]
        new_y = y + move_y * int(l)
        new_x = x + move_x * int(l)
        points.append((new_y, new_x))
    
    a = shoelace_area(points)
    b = sum([int(move[2][2:7], 16) for move in moves])

    return a - (b // 2) + 1 + b
                      


def main():
    digs = read_input('input.txt')
    print(calculate_area(digs))
    

if __name__ == '__main__':
    main()
            