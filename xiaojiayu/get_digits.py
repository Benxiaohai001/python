def get_digits(n):
    n = str(n)
    # l = [n[i] for i = 0 in n.length()]
    i = 0
    l = []
    while i < len(n):
        l.append(int(n[i]))
        i += 1
    return l
        
n = int(input('请输入一个数字：'))
print(get_digits(n))
