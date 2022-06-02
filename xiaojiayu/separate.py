f = open('e:/Python_ex/小甲鱼/2/record.txt')
#f1 = open('e:/Python_ex/小甲鱼/2/replace.txt','wt')
#f2 = open('e:/Python_ex/小甲鱼/2/part1.txt','wt')
girl = []
boy = []
count = 0
for each_line in f:
    #print(type(each_line))
    #st1 = each_line
    if each_line[:6] != '======':
        #f2.write(each_line)
        #print('111')
        if each_line[:1] == '燕':
            girl.append(each_line.split(':'))
        else:
            boy.append(each_line.split(':'))
    else:
        count += 1
        girl_file_name = 'girl_' + str(count) + '.txt'
        boy_file_name = 'boy_' + str(count) + '.txt'

        girl_file = open('e:/Python_ex/小甲鱼/2/' + girl_file_name,'w')
        boy_file = open('e:/Python_ex/小甲鱼/2/' + boy_file_name,'w')

        girl_file.writelines(girl)
        boy_file.writelines(boy)

        girl_file.close()
        boy_file.close()
        
    #else:
     #   break
# f2.close()
    
        #f1 = 
    #f1.write(each_line)


#f1.close()
f.close()
