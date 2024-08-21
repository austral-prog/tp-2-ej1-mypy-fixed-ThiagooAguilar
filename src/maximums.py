def max_of_two(x, y):
    biggest = x
    if x >= y:
        return biggest
    else:
        biggest = y
        return biggest

def max_of_three(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z


