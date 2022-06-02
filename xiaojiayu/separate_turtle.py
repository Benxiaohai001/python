f = open('e:/Python_ex/小甲鱼/2/record.txt')
boy = []
girl = []
count = 1
for each_line in f:
    if each_line[:6] == '======':
        (role,line_spoken) = each_line.split(':',1)
        if role == '小燕燕':
            girl.append(line_spoken)
        else:
            boy.append(line_spoken)
    else:
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'

        boy_file = open('e:/Python_ex/小甲鱼/2/' + file_name_boy + '.txt','w')
        girl_file = open('e:/Python_ex/小甲鱼/2/' + file_name_boy + '.txt','w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy = []
        girl = []

        count += 1



f.close()
