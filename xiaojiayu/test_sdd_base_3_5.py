def myfun(*p):
    add,result = 0,0
    if p[len(p)-1] == 5:
        for j in p:
            add += j
        result = add * 5
    else:
        for j in p:
            add += j
        result = add * 3
    print(result)


myfun(1,23,4,5)
myfun(3,4,5,6,7)
