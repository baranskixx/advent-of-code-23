def get_sum_from_file(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            digits = [int(char) for char in line if char.isdigit()]
            if len(digits) == 1:
                digits.append(digits[0])
            if digits:
                total_sum += digits[0] * 10 + digits[-1]
    return total_sum

if __name__ == '__main__':
    print(get_sum_from_file('input.txt'))