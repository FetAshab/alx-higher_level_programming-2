#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    
    high_keys = list(a_dictionary.keys())
    maxi = max(high_keys)
    return (maxi)
