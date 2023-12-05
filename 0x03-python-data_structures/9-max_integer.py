#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    big_num = my_list[0]
    for i in my_list:
        if big_num < i:
            big_num = i
    return big_num
