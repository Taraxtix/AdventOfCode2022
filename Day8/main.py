def parse_file(filename):
    with open(filename, 'r') as f:
        return [[int(tree) for tree in line.strip()] for line in f]


def is_visible(grid, pos):
    pos_x, pos_y = pos
    tree = grid[pos_x][pos_y]
    visible_from_top = True
    visible_from_left = True
    visible_from_bottom = True
    visible_from_right = True

    for x in range(pos_x):
        if grid[x][pos_y] >= tree:
            visible_from_top = False
            break

    for x in range(pos_x + 1, len(grid)):
        if grid[x][pos_y] >= tree:
            visible_from_bottom = False
            break

    for y in range(pos_y):
        if grid[pos_x][y] >= tree:
            visible_from_left = False
            break

    for y in range(pos_y + 1, len(grid[0])):
        if grid[pos_x][y] >= tree:
            visible_from_right = False
            break

    return visible_from_top or visible_from_bottom or visible_from_left or visible_from_right


def get_scenic_score(grid, pos) -> int:
    pos_x, pos_y = pos
    tree = grid[pos_x][pos_y]
    scenic_score = 1

    temp = 0
    for x in range(pos_x - 1, -1, -1):
        temp += 1
        if grid[x][pos_y] >= tree:
            break
    scenic_score *= temp

    temp = 0
    for x in range(pos_x + 1, len(grid)):
        temp += 1
        if grid[x][pos_y] >= tree:
            break
    scenic_score *= temp

    temp = 0
    for y in range(pos_y - 1, -1, -1):
        temp += 1
        if grid[pos_x][y] >= tree:
            break
    scenic_score *= temp

    temp = 0
    for y in range(pos_y + 1, len(grid[0])):
        temp += 1
        if grid[pos_x][y] >= tree:
            break
    scenic_score *= temp

    return scenic_score

def main(filename):
    grid = parse_file(filename)

    scenic_score = 0
    nb_visible_trees = 2 * len(grid) + 2 * len(grid[0]) - 4
    for x in range(1, len(grid)-1):  # Go through each line of the grid
        for y in range(1, len(grid[0])-1):  # Go through each tree in the line
            scenic_score = max(scenic_score, get_scenic_score(grid, (x, y)))
            if is_visible(grid, (x, y)):
                nb_visible_trees += 1

    print(f"Part1 : {nb_visible_trees}")
    print(f"Part2 : {scenic_score}")


if __name__ == "__main__":
    main('input.txt')
