

def answer(x, y):
    # first should be smaller
    x, y = (x, y) if len(x) < len(y) else (y, x)

    ids_set = set(x)

    for item in y:
        if item not in ids_set:
            return item