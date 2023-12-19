def read_input(path) -> list:
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines()]    


def process_points(points_data):
    points = []
    for line in points_data:
        pairs = line[1:-1].split(',')
        point_data = {}
        for pair in pairs:
            key, val = pair.split('=')
            point_data[key] = int(val)
        points.append(point_data)
    return points


def process_workflows(workflow_data):
    result = {}
    for workflow in workflow_data:
        open_bracket = workflow.index('{')
        key = workflow[:open_bracket]
        translations = workflow[open_bracket+1 : -1].split(',')
        val = []
        for t in translations[:-1]:
            cmp = t[1]
            cat = t[0]
            colon_index = t.index(':')
            num = int(t[2:colon_index])
            to = t[colon_index+1:]
            val.append((cat, cmp, num, to))
        val.append(translations[-1])

        result[key] = val
    return result


def meets_criteria(val, cmp, num):
    return val > num if cmp == '>' else val < num


def find_next_state(point, transfers):
    for cat, cmp, num, to in transfers[:-1]:
        if meets_criteria(point[cat], cmp, num):
            return to
    return transfers[-1]


def is_accepted(point, workflows):
    state = 'in'
    while state not in ['A', 'R']:
        transfers = workflows[state]
        state = find_next_state(point, transfers)
    return state == 'A'

        
def main():
    input = read_input('sample.txt')
    border = input.index('')
    points = process_points(input[border + 1:])
    workflows = process_workflows(input[:border])
    result = 0
    for p in points:
        if is_accepted(p, workflows):
            result += sum(p.values())
    print(result)




if __name__ == '__main__':
    main()