def main(infile):
    with open(infile) as file:
        str = file.readline()

    start_index = 0
    end_index = 0
    letters = [str[0]]

    while True:
        end_index +=1
        c = str[end_index]

        if letters.__contains__(c):
            index = letters.index(c)
            for _ in range(index + 1):
                letters.remove(letters[0])
                start_index += 1
        letters.append(c)
        if len(letters) == 14:
            break
    print(end_index + 1)




if __name__ == "__main__":
    main('input.txt')