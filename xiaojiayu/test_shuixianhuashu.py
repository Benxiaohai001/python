def shuixianhua():
    for x in range(100,1000):
        a = x // 100
        b = (x % 100) // 10
        c = (x % 10)
        if a ** 3 + b ** 3 + c ** 3 == x:
            print(x)



shuixianhua()
