#!/usr/bin/python3
def multiple_returns(sentence):
    result = ()
    if (sentence == ""):
        result = (0, None)
        return result
    else:
        result = (len(sentence), sentence[0])
        return result
