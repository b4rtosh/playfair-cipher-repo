def generate_matrix(provided_key):
    unrolled_matrix = []
    row = []
    if len(provided_key) < 25:
        for m in range(len(provided_key) // 5 + 1):
            row = []
            for n in range(5):
                letter = m * 5 + n
                if letter == len(provided_key):
                    break
                row.append(provided_key[letter])
                if len(row) == 5:
                    unrolled_matrix.append(row)
                    row = []
    for i in range(65, 91, 1):
        if chr(i) == 'J':
            continue
        elif chr(i) not in provided_key:
            row.append(chr(i))
            if len(row) == 5:
                unrolled_matrix.append(row)
                row = []
    print(unrolled_matrix)
    return unrolled_matrix


def cut_to_pairs(message):
    pair_letters = []
    i = int(0)
    while i < len(message):
        if i == len(message) - 1:
            pair_letters.append(message[i] + 'Z')
            i += 1
        elif message[i] != message[i + 1]:
            if message[i + 1] == ' ':
                pair_letters.append(message[i] + 'Z')
                i += 2
            elif message[i] == ' ':
                pair_letters.append('Z' + message[i + 1])
                i += 2
            else:
                pair_letters.append(message[i] + message[i + 1])
                i += 2
        else:
            pair_letters.append(message[i] + 'X')
            i += 1
    print(pair_letters)
    return pair_letters


def encode(code, given_message):
    pairs = cut_to_pairs(given_message)
    for i in range(len(pairs)):
        for x, letter in enumerate(code):
            if pairs[i][0] in letter:
                first_row, first_collumn = x, letter.index(pairs[i][0])
            if pairs[i][1] in letter:
                second_row, second_collumn = x , letter.index(pairs[i][1])
        if first_collumn == second_collumn:
            new_pair = code[first_row - 1][first_collumn] + code[second_row - 1][second_collumn]
            pairs[i] = new_pair
        elif first_row == second_row:
            new_pair = code[first_row][first_collumn - 1] + code[second_row][second_collumn - 1]
            pairs[i] = new_pair
        else:
            new_pair = code[first_row][second_collumn] + code[second_row][first_collumn]
            pairs[i] = new_pair
    encoded_message = str()
    for i in pairs: encoded_message += i
    return encoded_message


def decode(code, given_message):
    pairs = cut_to_pairs(given_message)
    for i in range(len(pairs)):
        for x, letter in enumerate(code):
            if pairs[i][0] in letter:
                first_row, first_collumn = x, letter.index(pairs[i][0])
            if pairs[i][1] in letter:
                second_row, second_collumn = x, letter.index(pairs[i][1])
        if first_collumn == second_collumn:
            new_pair = code[(first_row + 1) % 5][first_collumn] + code[(second_row + 1) % 5][second_collumn]
            pairs[i] = new_pair
        elif first_row == second_row:
            new_pair = code[first_row][(first_collumn + 1) % 5] + code[second_row][(second_collumn + 1) % 5]
            pairs[i] = new_pair
        else:
            new_pair = code[first_row][second_collumn] + code[second_row][first_collumn]
            pairs[i] = new_pair
    encoded_message = str()
    for i in pairs: encoded_message += i
    return encoded_message

if __name__ == '__main__':
    key = input("Enter key: ")
    matrix = generate_matrix(key)
    given_message = input("Enter message: ")
    given_message = encode(matrix, given_message)
    print("Encoded message: ", given_message)
    given_message = decode(matrix, given_message)
    print("Decoded message: ", given_message)
