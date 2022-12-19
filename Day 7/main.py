from Dir import Dir


def cd(dir_name: str, current_dir: Dir):
    if dir_name == "..":
        print("returned to parent dir")
        return current_dir.parent
    else:
        print(f"Go to dir : {dir_name}")
        return current_dir.found_dir_by_name(dir_name)


def ls(results: list[str], current_dir):
    results = [result.split(" ") for result in results]
    for result in results:
        if result[0] == 'dir':
            current_dir.add_dir(result[1])
            print(f"Added directory : {result[1]}")
        else:
            current_dir.add_file(result)
            print(f"Added file : {result[1]}")


def parse_command(command: list[str], current_dir: Dir):
    print(command)
    prompt: str = command[0]
    result: list[str] = command[1:]

    if prompt[:4] == "$ cd":
        current_dir = cd(prompt[5:], current_dir)
    else:
        ls(result, current_dir)
    print("--------------------------------------------")
    return current_dir


def parse_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    commands: list = []
    command: list = [lines[0]]
    for line in lines[1:]:
        if line[0] == '$':
            commands.append(command)
            command = [line]
            continue
        command.append(line)
    commands.append(command)
    return commands


def every_sub_dirs(dir: Dir):
    all_dirs: list[Dir] = []
    for sub_dir in dir.dirs:
        all_dirs.append(sub_dir)
        all_dirs.extend(every_sub_dirs(sub_dir))
    return all_dirs


def main(filename):
    commands = parse_file(filename)

    current_dir: Dir = Dir("/", None)
    root: Dir = current_dir

    for command in commands[1:]:
        current_dir = parse_command(command, current_dir)

    all_dirs: list[Dir] = [root]
    all_dirs.extend(every_sub_dirs(root))

    print(f"Part1 = {sum([dir.get_total_size() for dir in all_dirs if dir.get_total_size() <= 100000])}")

    space_needed = 30000000 - (70000000 - root.get_total_size())
    print(f"Part2 = {min([dir.get_total_size() for dir in all_dirs if dir.get_total_size() >= space_needed])}")


if __name__ == "__main__":
    main('input.txt')
