from aoc import read_input


def calculate_score(line):
    hand = line.split(" ")
    score = 0
    if hand[0] == hand[1]: score += 3

    if hand[0] == "A" and hand[1] == "B": score += 6
    if hand[0] == "B" and hand[1] == "C": score += 6
    if hand[0] == "C" and hand[1] == "A": score += 6

    if hand[1] == "A": score += 1
    if hand[1] == "B": score += 2
    if hand[1] == "C": score += 3

    return score


def part1():
    score_by_hand = []

    for line in data:
        line = line.replace("X", "A")
        line = line.replace("Y", "B")
        line = line.replace("Z", "C")
        score_by_hand.append(calculate_score(line))

    total_score = sum(score_by_hand)
    print(total_score)
    return total_score


# X = lost, Y = draw, Z = win
# A for Rock, B for Paper, and C for Scissors
def find_hand(line, win):
    hand = line.split(" ")

    if hand[0] == "A":
        response = "B" if win else "C"
        line = line.replace(hand[1], response)
    elif hand[0] == "B":
        response = "C" if win else "A"
        line = line.replace(hand[1], response)
    elif hand[0] == "C":
        response = "A" if win else "B"
        line = line.replace(hand[1], response)

    return line


def part2():
    score_by_hand = []

    for line in data:
        hand = line.split(" ")
        if hand[1] == "X":
            line = find_hand(line, False)
        elif hand[1] == "Y":
            line = line.replace("Y", hand[0])
        elif hand[1] == "Z":
            line = find_hand(line, True)

        score_by_hand.append(calculate_score(line))

    total_score = sum(score_by_hand)
    print(total_score)
    return total_score


data = read_input("day02", str)
print(part1())
print(part2())
assert (part1() == 12679)
assert (part2() == 14470)
