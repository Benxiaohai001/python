class Solution:
    def simplifyPath(self, path):
        path_item = path.split('/')
        str_ret = '/'
        len_pre = []
        for i in path_item:
            if i == '..':
                if str_ret == '/':
                    pass
                elif str_ret == '':
                    str_ret = '/'
                else:
                    if len_pre == []:
                        pass
                    else:
                        str_ret = str_ret[:-len_pre[-1]]
                        len_pre.pop()
            elif (i == '.') or (i == ''):
                pass
            else:
                if str_ret == '/':
                    str_ret = str_ret + i
                else:
                    str_ret = str_ret + '/' + i
            if len(i) == 0 or i == '.' or i == '..':
                pass
            else:
                len_pre.append(len(i) + 1)
            # path_item.remove(i)
        return str_ret


if __name__ == "__main__":
    s = Solution()
    print(s.simplifyPath("/home/of/foo/../../bar/../../is/./here/."))