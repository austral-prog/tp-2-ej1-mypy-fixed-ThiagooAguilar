def max_of_two(x, y):
    biggest = x
    if x >= y:
        return biggest
    else:
        biggest = y
        return biggest

# Replace the "ANSWER HERE" for your answer
def max_of_three(x, y, z):
    max = x
    if x > y and x>z:
        return max
    elif y>x and y>z:
        return max
    elif z>x and z>y:
        return max
    elif x=y:
        return max
    elif x=z:
        return max
    else:
        max=y
        return max


