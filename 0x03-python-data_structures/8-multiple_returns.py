#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return 0
    elif sentence[0] == None:
        return None
    else:
        return len(sentence), sentence[0]
