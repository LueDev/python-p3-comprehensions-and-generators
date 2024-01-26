#!/usr/bin/env python3

def return_evens(num_list):
    #The filter function accepts a function (anon included) and the target list.
    #The use is filter(customFunction, targetList) which returns a filter object.
    #Must wrap this with a list statement. list(filter(customFunc, targetList))
    evens = list(filter(lambda num: num % 2 == 0 and num >= 0, num_list))
    return evens

def make_exclamation(sentence_list):
    exclamation = lambda s : s + "!"
    return [exclamation(sentence) for sentence in sentence_list]
    