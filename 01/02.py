number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_number_word_starting_in_i(string, i):
    for index, word in enumerate(number_words, start=1):
        if i + len(word) < len(string) and string[i : i + len(word)] == word:
            return index + 1
    return -1

def get_sum_from_file(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            digits = [(int(line[x]), x) for x in range(len(line)) if line[x].isdigit()] + [(get_number_word_starting_in_i(line, x), x) for x in range(len(line))]
            digits = [elem for elem in digits if elem[0] != -1]
            digits = sorted(digits, key = lambda x : x[1])
            total_sum += digits[0][0] * 10 + digits[-1][0]
    
    return total_sum

if __name__ == '__main__':
    print(get_sum_from_file('input.txt'))