def group_by(func, iterable):
    mydict = {}
    for part in iterable:
        mydict.setdefault(func(part), []).append(part)
    return mydict


print(group_by(len, ['hi', 'bye', 'yo', 'try']))