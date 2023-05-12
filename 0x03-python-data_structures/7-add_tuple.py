#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add 2 tuples."""
    a, b = list(tuple_a), list(tuple_b)
    while len(a) < 2:
        a.append(0)
    while len(b) < 2:
        b.append(0)
    c = tuple([sum(i) for i in zip(a[:2], b[:2])])
    return(c)
