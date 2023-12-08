def read_input(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines() if line != '\n']

def load_graph(graph_lines):
    graph_right = {}
    graph_left  = {}
    for line in graph_lines:
        _from = line[0:3]
        left, right = line[7:10], line[12:15]
        graph_right[_from] = right
        graph_left[_from] = left

    return graph_left, graph_right

if __name__ == '__main__':
    lines = read_input('input.txt')
    seq = lines[0]
    graph_left, graph_right = load_graph(lines[1:])
    
    current_pos = 'AAA'
    current_move = 0
    steps = 0
    
    while current_pos != 'ZZZ':
        current_pos = graph_left[current_pos] if seq[current_move] == 'L' else graph_right[current_pos]
        current_move = (current_move + 1) % len(seq)
        steps += 1

    print(steps)