# Replace the "ANSWER HERE" for your answer
def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    year = int(input("Ingrese un año: "))
    is_leap = is_leap_year(year)
    print(f"El año {year} es {'bisiesto' if is_leap else 'no bisiesto'}")
    return is_leap

