# 1.要么怎样，要么怎样
'''
temp = input('请输入一个值：')

num = int(temp)

if num > 5:
    print('你输入的值大于5')
else:
    print('您输入的值，不小于5')
    
'''
# 2.干了怎样，不干怎样？
'''
temp = input('请输入一个值：')

num = int(temp)

count = num - 1

while count > 1:
    if num % count == 0:
        print('您输入的是和数！！！最大公因子：%d'%count)
        break
    count -= 1
else:
    print('您输入的是素数！！！')
'''

# 3.自动关闭文件，当文件不用的时候
try:
    temp = input('随便输入：')

    value = int(temp)
    
    # int('abc')
except ValueError as reason:
    print('出错了！！！' + str(reason))

else:
    print('没有出错')



# with的用法
'''
with open('woshinibaba.txt','w') as f:
    f.write('wocaishinibaba!!!')
''' 
