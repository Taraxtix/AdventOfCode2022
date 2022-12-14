def top1(elves_backpacks):

    max_calories = 0
    current = 0
    for element in elves_backpacks:
        if element == "":
            max_calories = max(max_calories, current)
            current = 0
            continue
        current += int(element)
    return max_calories


def recompute_top3(top3_elves, current):
    if current > top3_elves[0]:
        top3_elves[2] = top3_elves[1]
        top3_elves[1] = top3_elves[0]
        top3_elves[0] = current
        return top3_elves
    elif current > top3_elves[1]:
        top3_elves[2] = top3_elves[1]
        top3_elves[1] = current
        return top3_elves
    elif current > top3_elves[2]:
        top3_elves[2] = current
    return top3_elves


def top3(elves_backpacks):
    top3_elves = [0, 0, 0]
    current = 0
    for element in elves_backpacks:
        if element == "":
            top3_elves = recompute_top3(top3_elves, current)
            current = 0
            continue
        current += int(element)
        top3_value = 0
    for elve_backpack in top3_elves:
        top3_value += elve_backpack
    return top3_value


def main(input_file):
    with open(input_file) as f:
        file_content = f.read()

    elves_backpacks = file_content.split("\n")
    print(top3(elves_backpacks))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('input.txt')
