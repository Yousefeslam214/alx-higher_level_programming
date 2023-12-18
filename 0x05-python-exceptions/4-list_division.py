#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    result = []
    while list_length > 0:
        list_length -= 1
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except TypeError:
            result.append(0)
            print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")
        finally:
            i += 1
    return result
