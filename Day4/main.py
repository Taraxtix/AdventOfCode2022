def does_it_overlap(pair, need_to_fully_contains):
    task1 = [int(digit) for digit in pair[0].split('-')]
    task2 = [int(digit) for digit in pair[1].split('-')]

    if need_to_fully_contains:
        if (task1[0] >= task2[0] and task1[1] <= task2[1]) or (task2[0] >= task1[0] and task2[1] <= task1[1]):
            return 1
    else:
        if (task2[0] <= task1[0] <= task2[1]) or (task2[0] <= task1[1] <= task2[1]) or does_it_overlap(pair, True):
            return 1
    return 0


def how_many_overlap_task(pairs, need_to_fully_contains):
    cpt = 0
    for pair in pairs:
        cpt += does_it_overlap(pair, need_to_fully_contains)

    return cpt


def main(infile):
    with open(infile) as file:
        pairs = [line.strip().split(',') for line in file]

    print(f"Part1 : {how_many_overlap_task(lines, True)}")
    print(f"Part2 : {how_many_overlap_task(lines, False)}")


if __name__ == "__main__":
    main('input.txt')
