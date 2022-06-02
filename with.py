# f = open('./1.txt','wb')
f = open('./1.txt','w')

f.write('111')
try:
    f.write('Hello World!!!')# 当我在写内容的时候，这里因为是字符串，
    # 应该会报错的
    # 但是因为下一句把抓取的异常都pass了，所以没有报错，但是也没写内容。


except:
    pass

finally:
    f.close()

# f.close()
