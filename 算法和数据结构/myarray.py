# 1. 插入，删除，随机访问
# 2. 数据类型为整形
# 
# author：xx


class Myarray:
    """
    对列表的简单封装；
    不能使用-1
    """

    def __init__(self, capacity) -> None:
        self._data = []   # 直接调用的python的列表
        self._capacity = capacity
    
    def __getitem__(self, position):
        return self._data[position]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item
    
    def find(self, index):
        try:
            return self._data[index]
        except IndexError:
            return None
    
    


