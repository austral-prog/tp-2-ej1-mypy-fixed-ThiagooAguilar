def main(year: int) -> bool:
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

def is_leap_year() -> bool:
    año = int(input("Ingrese un año: "))
    is_leap = main(año)
    if is_leap:
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")
    return is_leap
