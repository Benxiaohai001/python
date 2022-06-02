def leapYear():
    y = 2020
    ly = []
    while y:
        if ((y%4 == 0 and y%100 != 0) or (y%400 == 0)):
            ly.append(y)
        y -= 1
    return ly

leapYear()
