#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        first = sentence[0]
        return len(sentence), sentence[0]
    else:
        return(0, None)
