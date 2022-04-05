def mutate_string(string, position, character):
    # list_1 = list(s)
    # list_1[int(i)] = str(c)
    # answer = ''.join(list_1)
    n = int(i) + 1
    list_2 = s[:int(i)] + c + s[int(n):]

    return list_2


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)