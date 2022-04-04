def split_and_join(line):
    word = line.split(" ")
    word = "-" .join(word)
    return word


if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result