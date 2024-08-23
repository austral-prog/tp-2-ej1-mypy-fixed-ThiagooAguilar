# Replace the "ANSWER HERE" for your answer
def is_leap_year():
    my_year=int(input("Ingrese un año: "))
    if ((my_year%4 == 0) and (my_year%100 !=0)):
        return True
    elif ((my_year%100==0) and (my_year%400==0)):
        return True
    else:
        return False
