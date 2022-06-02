def binary(n):
    s = s0 = '0'
    if n == 1:
        s = '1'# 如果是一，直接返回‘1’
    else:
        s0 = str(n%2)# 先求出尾数
        #binary(n//2)
        s = binary(n//2) + s0
        #s = '1'+s0
    return s


n = int(input('请输入一个数字：'))
result = binary(n)
print('binary(n) = %s'%result)
