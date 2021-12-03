def part_1(deck_1, deck_2):
    while deck_1 and deck_2:
        print(f'{deck_1 = }')
        print(f'{deck_2 = }')
        if deck_1[0] > deck_2[0]:
            deck_1.append(deck_1.pop(0))
            deck_1.append(deck_2.pop(0))
        else:
            deck_2.append(deck_2.pop(0))
            deck_2.append(deck_1.pop(0))

        print()

    print('--- answer ---')
    print(deck_1)
    print(deck_2)

    score = 0

    for i in range(len(deck_2), 0, -1):
        print(f'{i = }')
        print(f'{deck_2[i * (-1)] = }')
        print(f'{i * deck_2[i * (-1)] = }')
        score += i * deck_2[i * (-1)]
        print()

    return score



if __name__ == '__main__':
    with open('/Users/anorsoni/Documents/Programmability/Advent of Code/2020/Day 22/player_1') as file:
        deck_1 = [int(i) for i in file.read().splitlines()]

    with open('/Users/anorsoni/Documents/Programmability/Advent of Code/2020/Day 22/player_2') as file:
        deck_2 = [int(i) for i in file.read().splitlines()]

    print('score = ', part_1(deck_1, deck_2))