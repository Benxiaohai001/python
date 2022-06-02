import re
a = 'not 404 found 张三 99 深圳'
list = a.split(' ')
print(list)
res = re.findall('\d+|[a-zA-Z]+',a)
# res = re.findall('\d + |[a-zA-Z] +',a) 对空格很敏感，如果有空格将会是另一个意思
for i in res:
    if i in list:
        list.remove(i)
new_str = ' '.join(list)
print(res)
print(new_str)
