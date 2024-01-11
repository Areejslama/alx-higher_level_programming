#!/usr/bin/python3
def best_score(a_dictionary):
    if  not a_dictionary:
        return None
    new_dic = list(a_dictionary.keys())
    max_v = 0
    l = ""
    for i in new_dic:
        if a_dictionary[i] > max_v:
            max_v = a_dictionary[i]
            l = i
    return l
