
BOX_COUNT = 256
HASH_MULTIPLIER = 17

def read_input(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def str_hash(str):
    val = 0
    for char in str:
        val = ((val + ord(char)) * HASH_MULTIPLIER) % BOX_COUNT
    return val

def operation_type(str):
    return '=' if '=' in str else '-'

def multiplier(str):
    return int(str[-1]) if str[-1].isdigit() else None

def get_boxes_after_all_steps(steps):
    boxes = [[] for _ in range(BOX_COUNT)]

    for label, hash, op, mult in steps:
        box = boxes[hash]
        if op == '=':
            for i, elem in enumerate(box):
                if elem[0] == label:
                    box[i] = (label, mult)
                    break
            else:
                box.append((label, mult))
        else:
            boxes[hash] = [elem for elem in box if elem[0] != label]
    return boxes

def calculate_total_boxes_value(boxes):
    result = 0
    for box_index, box in enumerate(boxes):
        for elem_index, elem in enumerate(box):
            _, mult = elem
            result += (box_index + 1) * (elem_index + 1) * mult
    return result


if __name__ == '__main__':
    data = read_input('input.txt')
    sequence = data[0].split(',')
    steps = []
    for elem in sequence:
        op = operation_type(elem)
        m = multiplier(elem)
        h = str_hash(elem[:-1]) if op == '-' else str_hash(elem[:-2])
        label = elem[:-1] if op == '-' else elem[:-2]
        steps.append((label, h, op, m))

    final_boxes = get_boxes_after_all_steps(steps)
    final_result = calculate_total_boxes_value(final_boxes)
    print(final_result)