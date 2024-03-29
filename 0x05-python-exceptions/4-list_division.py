#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    n = 0
    for i in range(list_length):
        try:
            result = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            n += 1
            new_list.append(result)
    return new_list
