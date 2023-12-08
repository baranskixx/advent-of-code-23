from copy import copy
import math

def nww(a, b):
    return (a * b) // math.gcd(a, b)

def nww_list(lista):
    if len(lista) < 2:
        raise ValueError("Lista musi zawierać co najmniej dwie liczby")

    nww_result = lista[0]
    for i in range(1, len(lista)):
        nww_result = nww(nww_result, lista[i])
    
    return nww_result


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

def find_next_final_field(seq, graph_left, graph_right):
    next_final = {}
    for field in graph_left.keys():
        curr_field = field
        i = 0
        steps = 0
        while True:
            curr_field = graph_left[curr_field] if seq[i] == 'L' else graph_right[curr_field]
            i = (i+1) % len(seq)
            steps += 1
            if curr_field.endswith('Z'):
                break
        next_final[field] = (curr_field, steps)
    
    return next_final

if __name__ == '__main__':
    lines = read_input('input.txt')
    seq = lines[0]
    graph_left, graph_right = load_graph(lines[1:])
    
    starting_positions = [pos for pos in graph_right.keys() if pos.endswith('A')]
    current_positions = copy(starting_positions)
    next_final = find_next_final_field(seq, graph_left, graph_right)

    next_finals_for_start = [next_final[pos][1] for pos in starting_positions]
    print(next_finals_for_start)

    print(nww_list(next_finals_for_start))