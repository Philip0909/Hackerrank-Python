def swap_case(s):
    list_s = list(s)
    answer_list = []
    print(list_s)
    for element in list_s:
        if element.islower():
            answer_list.append(element.upper())
        else:
            answer_list.append(element.lower())

    return "".join(answer_list)
