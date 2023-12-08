def read_input(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines() if line != '\n']

ranks = "AKQT98765432J"

def evaluate_hand(hand):
    count = [0] * 14
    js = 0
    for card in hand:
        if card == 'J':
            js += 1
        else:
            count[ranks.index(card)] += 1

    max_count = max(count)
    if max_count == 0:
        count[0] = 5
        print('J')
        print(count)
    else:
        max_count_index = count.index(max_count)
        count[max_count_index] += js
    max_count = max(count)

    if max_count == 5:
        return 6  # Five of a kind
    elif max_count == 4:
        return 5  # Four of a kind
    elif max_count == 3:
        if count.count(2) == 1:
            return 4  # Full house
        else:
            return 3  # Three of a kind
    elif max_count == 2:
        if count.count(2) == 2:
            return 2  # Two pair
        else:
            return 1  # One pair
    else:
        return 0  # High card

def calculate_total_winnings(hands, bids):
    hand_rankings = [[evaluate_hand(hands[i]), -ranks.index(hands[i][0]), -ranks.index(hands[i][1]), \
                    -ranks.index(hands[i][2]), -ranks.index(hands[i][3]), -ranks.index(hands[i][4]), \
                    bids[i]] for i in range(len(hands))]
    hand_rankings.sort(reverse=True, key= lambda x : x[0:6])
    total_winnings = 0
    for index, rank in enumerate(hand_rankings):
        total_winnings += rank[6] * (len(hand_rankings) - index)
    
    return total_winnings

# Example input
if __name__ == '__main__':
    lines = read_input('input.txt')
    hands = [line.split()[0] for line in lines]
    bids = [int(line.split()[1]) for line in lines]
    
    total_winnings = calculate_total_winnings(hands, bids)
    print(total_winnings)
