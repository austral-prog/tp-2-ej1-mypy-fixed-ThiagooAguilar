# Replace the "ANSWER HERE" for your answer
def is_leap_year():
    my_year = int(input("Insert year: "))

    if (my_year % 4 == 0) and (my_year % 100 != 0):
        return f"El año {my_year} es bisiesto"
    elif (my_year % 100 == 0) and (my_year % 400 == 0):
        return f"El año {my_year} es bisiesto"
    else:
        return f"El año {my_year} no es bisiesto"
