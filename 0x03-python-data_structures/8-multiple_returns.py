#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == []:
        sentence.append(None)
    else:
        return len(sentence), sentence[0]
