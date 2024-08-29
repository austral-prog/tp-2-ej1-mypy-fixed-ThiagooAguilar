def max_of_two(x: int, y: int) -> int:
    biggest = x
    if x >= y:
        return biggest
    else:
        biggest = y
        return biggest
def max_of_three(x: int, y: int, z: int)-> int:
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

