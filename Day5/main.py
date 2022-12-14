def do_moves_3000(stacks, move):
    to_move = stacks[move[1]-1][:move[0]]
    destination = stacks[move[2]-1].copy()

    stacks[move[2]-1] = to_move[::-1]

    for item in destination:
        stacks[move[2]-1].append(item)

    for item in to_move:
        stacks[move[1]-1].remove(item)


def do_moves_3001(stacks, move):
    to_move = stacks[move[1]-1][:move[0]]
    destination = stacks[move[2]-1].copy()

    to_move_inverted = to_move[::-1]
    stacks[move[2] - 1] = to_move_inverted[::-1]

    for item in destination:
        stacks[move[2]-1].append(item)

    for item in to_move:
        stacks[move[1]-1].remove(item)


def main(infile):
    STACKS_NUMBER = 3 if infile == 'demo_input.txt' else 9

    with open(infile) as file:
        lines = [line.removesuffix('\n') for line in file]

    start_index = 0
    stacks_3000 = []
    stacks_3001 = []
    for line in lines:
        if line[1] == '1':
            start_index = lines.index(line) + 2
            break
        stacks_3000.append(line)
        stacks_3001.append(line)

    stacks_3000 = [[stack[i] for stack in stacks_3000 if i < len(stack) and stack[i] != ' ' ]
              for i in range(1, STACKS_NUMBER * 4, 4)]
    stacks_3001 = [[stack[i] for stack in stacks_3001 if i < len(stack) and stack[i] != ' ']
                   for i in range(1, STACKS_NUMBER * 4, 4)]
    moves = [list(map(int, [line[5:-12], line[-6:-5], line[-1:]])) for line in lines[start_index:]]

    for move in moves:
        do_moves_3000(stacks_3000, move)
        do_moves_3001(stacks_3001, move)

    print(f"Part 1 : ", end='')
    for stack in stacks_3000:
        if len(stack) == 0:
            continue
        print(f"{stack[0]}", end='')

    print()

    print(f"Part 2 : ", end='')
    for stack in stacks_3001:
        if len(stack) == 0:
            continue
        print(f"{stack[0]}", end='')

if __name__ == '__main__':
    main('input.txt')