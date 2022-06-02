shuru = input('请输入文件名')
f = open('e:/Python_ex/小甲鱼/2/' + shuru,'w')
while 1:
    wenzi = input('请输入内容（：w退出）：')
    if wenzi == ':w':
        f.close()
        break
    else:
        f.writelines(wenzi)
