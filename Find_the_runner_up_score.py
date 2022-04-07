if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    list_arr = list(arr)

    winner = -100
    runner_up = -100
    for i in list_arr:
        if i > winner:
            winner = i

    for i in list_arr:

        if i == winner:
            continue
        elif i > runner_up:
            runner_up = i

    print(runner_up)

