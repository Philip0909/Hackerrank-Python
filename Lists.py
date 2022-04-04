if __name__ == '__main__':

    N = int(input())
    list_1 = []
    for i in range(0, N):
        message = input()
        cmd = message.split(' ')[0]
        if cmd == 'insert':
            num_1 = message.split(' ')[1]
            num_2 = message.split(' ')[2]
            list_1.insert(int(num_1), int(num_2))
        elif cmd == 'remove':
            num_1 = message.split(' ')[1]
            list_1.remove(int(num_1))

        elif cmd == 'append':
            num_1 = message.split(' ')[1]
            list_1.append(int(num_1))

        elif cmd == 'remove':
            num_1 = message.split(' ')[1]
            list_1.remove(int(num_1))

        elif cmd == 'sort':
            list_1.sort()

        elif cmd == 'pop':
            list_1.pop()

        elif cmd == 'reverse':
            list_1.reverse()

        elif cmd == 'print':
            print(list_1)
