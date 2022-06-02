dict = {'name':'PJ','age':23,'city':'ShenZhen','tel':'18434391963'}
list = sorted(dict.items(),key = lambda i:i[0],reverse = False)
print(type(list))
# list内是什么？tuple吗？
print(type(list[0]))
print('sorted根据字典排序',list)
new_dict = {}
for i in list:
    new_dict[i[0]] = i[1]
print('新字典',new_dict)
