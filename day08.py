from aoc import read_input


def score_east(r, c, height):
    i = 1
    score = 0
    while c+i < max_col:
        score += 1
        if tree_heights[r][c+i] >= height:
            return False, score
        i += 1
    return True, score


def score_west(r, c, height):
    i = 1
    score = 0
    while c-i >= 0:
        score += 1
        if tree_heights[r][c-i] >= height:
            return False, score
        i += 1
    return True, score


def score_north(r, c, height):
    i = 1
    score = 0
    while r-i >= 0:
        score += 1
        if tree_heights[r-i][c] >= height:
            return False, score
        i += 1
    return True, score


def score_south(r, c, height):
    i = 1
    score = 0
    while r+i < max_row:
        score += 1
        if tree_heights[r+i][c] >= height:
            return False, score
        i += 1
    return True, score


def is_tree_visible(r, c, height):
    return score_north(r, c, height)[0] or score_south(r, c, height)[0] or score_east(r, c, height)[0] or score_west(r, c, height)[0]


def scenic_score(r, c, height):
    return score_north(r, c, height)[1] * score_south(r, c, height)[1] * score_east(r, c, height)[1] * score_west(r, c, height)[1]


def find_visible_trees_with_scenic_scores():
    scenic_scores = []
    for r in range(max_row):
        for c in range(max_col):
            height = tree_heights[r][c]
            if is_tree_visible(r, c, height):
                scenic_scores.append(scenic_score(r, c, height))
    return scenic_scores


lines = read_input("day08", str)
max_row = len(lines)
max_col = len(lines[0])
tree_heights = [[0 for c in range(max_col)] for r in range(max_row)]
for r in range(max_row):
    for c in range(max_col):
        tree_heights[r][c] = int(lines[r][c])

scores = find_visible_trees_with_scenic_scores()

p1 = len(scores)
print(p1)
assert (p1 == 1708)
p2 = max(scores)
print(p2)
assert (p2 == 504000)