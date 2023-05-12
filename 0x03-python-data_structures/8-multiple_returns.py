#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns tuple, sentence length & first char."""
    if len(sentence) == 0:
        return(len(sentence), None)
    return(len(sentence), sentence[0])
