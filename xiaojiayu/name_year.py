
#方法一：
count = 0
length = len(member)
while count < length:
    print(member[count], member[count+1])
    count += 2

#方法二：    
'''  
for each in range(len(member)):
    if each%2 == 0:
        print(member[each], member[each+1])


'''


'''
member = ['小甲鱼',88,'黑夜',90,'迷途',85,'怡静',90,'秋舞斜阳',88]
count = 0
for i in member:
    while 1:
        i = str(i)
        print(i + ' ')


''''
'''
for i in member:# 这里的i为什么是int类型呢？88是int
    i = str(i)
    print(i + ' ')
    count += 1
    if count > 1:
        count = 0
'''
