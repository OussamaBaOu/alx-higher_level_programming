#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = []
    for b in range(0, list_length):
        try:
            c = my_list_1[b] / my_list_2[b]
        except TypeError:
            print("wrong type")
            c = 0
        except ZeroDivisionError:
            print("division by 0")
            c = 0
        except IndexError:
            print("out of range")
            c = 0
        finally:
            a.append(c)
    return (a)
