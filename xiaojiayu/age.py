def age(n):
    if n == 1:
        a = 10
    else:
        g = 2
        # age(n -1)
        a = age(n - 1) + g
    return a


n = int(input('你想知道第几个人的年龄：'))
print('第%d个人的年龄是%d岁'%(n,age(n)))
