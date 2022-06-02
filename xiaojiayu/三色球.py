z = 2
while z < 7:
    y = 0
    while y < 4:
        x = 8 - z - y
        if 0 <= x <= 3:
            print('Red %d, Yellow %d, Green %d'%(x,y,z))
        y += 1
    z += 1
