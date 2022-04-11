T = int(input())

for i in range(1, T + 1):
    a = input()
    new_a = a.split()
    div_a = (new_a[0])
    div_b = (new_a[1])
    try:
        print(int(div_a) // int(div_b))
    # except ZeroDivisionError:
    #     print('Error Code: integer division or modulo by zero')
    # except ValueError:
    #     print("Error Code: invalid literal for int() with base 10:" + " " "'{}'".format(div_b))
    except Exception as e:
        print('Error Code:', e)
