def group_by(func, iterable):
    dictionary = {}
    for part in iterable:
        dictionary.setdefault(func(part), []).append(part)
    return dictionary


if __name__ == "__main__":
    print(group_by(len, ['hi', 'bye', 'yo', 'try']))