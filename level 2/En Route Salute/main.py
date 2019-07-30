def answer(s):
    going_right = 0
    salutes = 0
    for ch in s:
        if ch == '>':
            going_right += 1
        elif ch == '<':
            salutes += 2 * going_right

    return salutes
