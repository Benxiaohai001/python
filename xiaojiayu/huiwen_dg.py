def huiwen_dg(s):
    if len(s) > 1:
        if s[0] == s[-1]:
            print('您输入的是回文')
        else:
            print('您输入的不是回文')
            break
    else:
        huiwen_dg(s[1:len(s)-1])
s = input('请输入一个回文字符串：')
huiwen_dg(s)
