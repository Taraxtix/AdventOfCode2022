PRIORITY_VALUES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
"""Each index of a char represents it's priority value - 1"""

def priority_v1(backpack):
    """Compute the priority of the missplaced items in the given backpack (FOR PART1)"""
    for c in backpack[:len(backpack)//2]:
        if c in backpack[len(backpack)//2:]:
            return PRIORITY_VALUES.index(c) + 1
    return 0


def priority_v2(backpacks_group):
    """Compute the priority of the common item in the backpack group (FOR PART2)"""
    for c in backpacks_group[0]:
        if c in backpacks_group[1] and c in backpacks_group[2]:
            return PRIORITY_VALUES.index(c) + 1
    return 0


def priorities_list(backpacks):
    """Create the list of the priority for each group of backpacks"""
    priorities = []
    for i in range(0, len(backpacks), 3):
        priorities.append(priority_v2([backpacks[i], backpacks[i+1], backpacks[i+2]]))

    return priorities


def main(input_file):
    with open(input_file) as f:
        backpacks = [str.strip() for str in f.readlines()]

    part1 = sum([priority_v1(backpack) for backpack in backpacks])
    part2 = sum(priorities_list(backpacks))

    print(f'Part 1 : {part1}')
    print(f'Part 2 : {part2}')


if __name__ == "__main__":
    main('input.txt')
