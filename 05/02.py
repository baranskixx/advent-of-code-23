from copy import copy

def read_input(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines() if line != '\n']

def intercepts(a_start, a_end, b_start, b_end):
    return max(a_start, b_start) < min(a_end, b_end)

def intersection(a_start, a_end, b_start, b_end):
    start = max(a_start, b_start)
    end = min(a_end, b_end)

    if start < end:
        return [start, end]
    else:
        return None

def difference(a_start, a_end, b_start, b_end):
    diff = []

    if a_start < b_start:
        diff.append((a_start, min(a_end, b_start)))
    if b_end < a_end:
        diff.append((max(a_start, b_end), a_end))

    return diff

if __name__ == '__main__':
    lines = read_input('input.txt')
    input_seeds = [int(number) for number in lines[0][7:].split()]
    input_intervals = [[input_seeds[i], input_seeds[i] + input_seeds[i+1]] for i in range(0, len(input_seeds), 2)]
    next_gen_intervals = []
    for i in range(2, len(lines)):
        line = lines[i]
        print(line)
        if line.endswith(':') or line == '-':
            input_intervals += next_gen_intervals
            next_gen_intervals = []
        else:
            dest_start, src_start, interval_width = [int(num_str) for num_str in line.split()]
            dest_end, src_end = dest_start + interval_width, src_start + interval_width
            x = 0
            while x < len(input_intervals):
                section_start, section_end = input_intervals[x]
                if intercepts(src_start, src_end, section_start, section_end):
                    inter_start, inter_end = intersection(src_start, src_end, section_start, section_end)
                    print(inter_start, inter_end)
                    diff = difference(section_start, section_end, src_start, src_end)
                    for elem in diff:
                        input_intervals.append(elem)
                    input_intervals.pop(x)
                    diff_src_dest = dest_start - src_start
                    next_gen_intervals.append([inter_start + diff_src_dest, inter_end + diff_src_dest])
                else:
                    x += 1
        print(input_intervals, next_gen_intervals)
    
    print(min(input_intervals, key = lambda x : x[0]))

                    
